from collections import namedtuple
from dataclasses import dataclass


@dataclass
class BudgetsTable:
    COLS = namedtuple("COLS", ("DB", "DISP"))
    TABLE_NAME = "budget"
    BUDGET_SCOPE_ID = COLS("budget_scope_id", "Budget Scope ID")
    USAGE_UPDATED_AT = COLS("usage_updated_at", "Usage Updated At")
    BUDGET_SCOPE = COLS("budget_scope", "Budget Scope")
    BUDGET = COLS("budget", "Budget")
    BUDGET_USAGE = COLS("budget_usage", "Budget Usage")
