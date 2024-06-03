from dash import Input, Output, State, ctx
from dash.exceptions import PreventUpdate
import dash
import time

from src.pages.procs.budgets_proc import budgets_table
from src.pages.layouts import budgets_layout
from src.routing import BUDGET

dash.register_page(__name__, path=BUDGET.ROUTE, name=BUDGET.TITLE)

layout = budgets_layout.layout


@dash.callback(
    Output(f"{BUDGET.ROUTE}_grid", "filterModel"),
    Input(f"{BUDGET.ROUTE}_clear_filter", "n_clicks"),
    prevent_initial_call=True,
)
def clear_filter(n_clicks):
    if n_clicks:
        time.sleep(0.3)
        return {}
    raise PreventUpdate


@dash.callback(
    Output(f"{BUDGET.ROUTE}_tags_input", "data"),
    Input("redirect", "pathname"),
)
def tags_dropdown_callback(_):
    return budgets_table.get_tags()


@dash.callback(
    Output(f"{BUDGET.ROUTE}_msg", "children"),
    Output(f"{BUDGET.ROUTE}_table", "children"),
    Input("redirect", "pathname"),
    Input(f"{BUDGET.ROUTE}_refresh_data", "data"),
    State(f"{BUDGET.ROUTE}_grid", "filterModel"),
)
def generate_table_callback(_1, _2, filter_model):
    return "", budgets_table.generate_table(filter_model)


@dash.callback(
    Output(f"{BUDGET.ROUTE}_msg", "children", allow_duplicate=True),
    Output(f"{BUDGET.ROUTE}_refresh_data", "data"),
    Input(f"{BUDGET.ROUTE}_apply_button", "n_clicks"),
    State(f"{BUDGET.ROUTE}_grid", "virtualRowData"),
    State(f"{BUDGET.ROUTE}_tags_input", "value"),
    prevent_initial_call=True,
)
def update_table_callback(clicks, table, tag_input):
    if clicks and tag_input:
        msg, refresh = budgets_table.update_table(table, tag_input)
        return msg, refresh
    raise PreventUpdate
