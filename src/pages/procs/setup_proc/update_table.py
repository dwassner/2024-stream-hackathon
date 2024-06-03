import dash
from src.helpers import db_funcs

from schemas.alerts_setup import AlertsTable
from schemas.shared import Shared


def update_data(users, new_tags, tags_to_delete, alerts_for, all_tags, alerts_value):
    if not alerts_for:
        return "Missing tags to alert", dash.no_update
    if tags_to_delete:
        if any([t in alerts_for for t in tags_to_delete]):
            return "Cannot remove tag present in Alerts for dropdown", dash.no_update
    if not users:
        return "Missing slack users", dash.no_update

    users = ",".join(users)
    alerts_for = ",".join(alerts_for)
    if new_tags:
        all_tags += new_tags.split(",")
    if tags_to_delete:
        all_tags = [t for t in all_tags if t not in tags_to_delete]

    all_tags = ",".join([t.strip() for t in all_tags if t and t.strip])

    query = f"""
        INSERT INTO {AlertsTable.TABLE_NAME} (
            {Shared.BRAND.DB},
            {AlertsTable.TAGS.DB},
            {AlertsTable.SLACK_USERS.DB},
            {AlertsTable.ALERTS_FOR.DB},
            {AlertsTable.ALERTS_VALUE.DB}
        )
        VALUES ("brand_a", "{all_tags}", "{users}", "{alerts_for}", {alerts_value})
        ON DUPLICATE KEY UPDATE
        {AlertsTable.TAGS.DB}="{all_tags}",
        {AlertsTable.SLACK_USERS.DB}="{users}",
        {AlertsTable.ALERTS_FOR.DB}="{alerts_for}",
        {AlertsTable.ALERTS_VALUE.DB}={alerts_value}
    """
    _, e = db_funcs.execute_sql(query)
    if e:
        return f"Error: {e}", dash.no_update
    return "Saved successfully!", True
