from collections import namedtuple
from dataclasses import dataclass


@dataclass
class AlertsTable:
    COLS = namedtuple("COLS", ("DB", "DISP"))
    TABLE_NAME = "alerts_setup"
    TAGS = COLS("all_tags", "Tags")
    SLACK_USERS = COLS("slack_users", "Slacks Users")
    ALERTS_FOR = COLS("alerts_for", "Alerts for")
    ALERTS_VALUE = COLS("alerts_value", "Alerts Value")
