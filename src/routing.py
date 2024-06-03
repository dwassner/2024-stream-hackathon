from collections import namedtuple

pages_and_routes = namedtuple("pages_and_routes", ["ICON", "TITLE", "ROUTE"])

HOME = pages_and_routes(None, "Armory", "/")
PLACEMENTS = pages_and_routes("arcticons:workplace", "Placements", "/placements")
BUDGET = pages_and_routes("arcticons:budgetmylife", "Budgets", "/budgets")
SETUP = pages_and_routes("material-symbols:settings", "Setup", "/setup")
