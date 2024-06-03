from src.constants import StrategyTypes as Strats
from src.helpers import db_funcs

from schemas.alerts_setup import AlertsTable
from schemas.shared import Shared


def fetch_data():
    query = f"""
        SELECT * FROM {AlertsTable.TABLE_NAME} WHERE {Shared.BRAND.DB} = "brand_a"
    """
    df, e = db_funcs.db_to_df(query)
    if df.empty:
        return Strats.ALL, Strats.ALL, None, None, 80

    row = df.iloc[0]
    tags = sorted(row[AlertsTable.TAGS.DB].split(","), key=str.casefold)
    return (
        tags,
        tags,
        row[AlertsTable.ALERTS_FOR.DB].split(","),
        row[AlertsTable.SLACK_USERS.DB].split(","),
        row[AlertsTable.ALERTS_VALUE.DB],
    )
