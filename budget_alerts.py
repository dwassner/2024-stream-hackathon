import os
import dotenv

from src.helpers.slack import send_slack_dm, create_dict_of_active_slack_users
from src.helpers import db_funcs

from schemas.campaigns import CampaignsListTable as Camps
from schemas.alerts_setup import AlertsTable
from schemas.budgets import BudgetsTable
from schemas.shared import Shared

dotenv.load_dotenv()


def get_budget_df(tags):
    tags = ", ".join([f"'{tag}'" for tag in tags.split(",")])
    query = f"""
        SELECT
            c.{Shared.CAMPAIGN_ID.DB},
            c.{Camps.NAME.DB},
            b.{BudgetsTable.BUDGET.DB},
            b.{BudgetsTable.BUDGET_USAGE.DB},
            b.{BudgetsTable.USAGE_UPDATED_AT.DB}
        FROM brand_a_{Camps.TABLE_NAME} as c
        LEFT JOIN brand_a_{BudgetsTable.TABLE_NAME} as b
            ON c.{Shared.CAMPAIGN_ID.DB} = b.{BudgetsTable.BUDGET_SCOPE_ID.DB}
        WHERE
            b.{BudgetsTable.BUDGET_SCOPE.DB}="CAMPAIGN" AND
            c.{Camps.TAG_1.DB} IN ({tags})
    """
    df, e = db_funcs.db_to_df(query)
    if e:
        return e
    return df


def get_campaigns_with_over_budget(tags, budget_limit):
    budget_df = get_budget_df(tags)
    budget_df = budget_df.loc[
        budget_df.groupby(Shared.CAMPAIGN_ID.DB).usage_updated_at.idxmax()
    ]
    over_limit_df = budget_df[BudgetsTable.BUDGET_USAGE.DB] > budget_limit

    return budget_df[over_limit_df][
        [Camps.NAME.DB, BudgetsTable.BUDGET_USAGE.DB]
    ].values.tolist()


def prepare_msg(campaigns, budget_limit):
    msg = (
        "Hello!\n\n"
        f"The following Campaigns are above {int(budget_limit)}% of daily budget\n"
        "BUDGET USED (%)\t\tCAMPAIGN\n"
    )
    for camp in campaigns:
        msg += f"\t{camp[1]:15.1f}\t\t\t\t\t{camp[0]}\n"
    return msg


def get_alerts():
    query = f"SELECT * FROM {AlertsTable.TABLE_NAME}"
    df, _ = db_funcs.db_to_df(query)
    return df


def main():
    df = get_alerts()
    for _, row in df.iterrows():
        campaigns = get_campaigns_with_over_budget(
            row[AlertsTable.ALERTS_FOR.DB],
            row[AlertsTable.ALERTS_VALUE.DB],
        )
        message = prepare_msg(campaigns, row[AlertsTable.ALERTS_VALUE.DB])
        if not os.getenv("slack_key"):
            print("No slack key set in env!!")
            print("Printing alert message here\n")
            print(message)
            return

        slack_users = create_dict_of_active_slack_users()
        if "Slack API is currently busy" in slack_users:
            print(slack_users)
            return
        for user in row[AlertsTable.SLACK_USERS.DB].split(","):
            slack_id = slack_users.get(user)
            send_slack_dm(slack_id, message)
            print(f"Slack message sent; User: {user}")


if __name__ == "__main__":
    main()
