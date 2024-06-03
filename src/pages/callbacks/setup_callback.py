from dash import Input, Output, State, ctx, clientside_callback, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash

from src.helpers.slack import create_list_of_active_slack_usersnames
from src.pages.procs.setup_proc.update_table import update_data
from src.pages.procs.setup_proc.fetch import fetch_data
from src.pages.layouts import setup_layout
from src.routing import SETUP

dash.register_page(__name__, path=SETUP.ROUTE, name=SETUP.TITLE)

layout = setup_layout.layout


@dash.callback(
    Output(f"{SETUP.ROUTE}_slack_drpdwn", "data"),
    Output(f"{SETUP.ROUTE}_slack_users", "data"),
    Input("redirect", "pathname"),
    State(f"{SETUP.ROUTE}_slack_users", "data"),
)
def slack_users_callback(_, slack_users):
    if not slack_users:
        slack_users = create_list_of_active_slack_usersnames()
    return slack_users, slack_users


@dash.callback(
    Output(f"{SETUP.ROUTE}_tags_input", "value"),
    Output(f"{SETUP.ROUTE}_tags_to_delete", "data"),
    Output(f"{SETUP.ROUTE}_tags_to_alert_drpdwn", "data"),
    Output(f"{SETUP.ROUTE}_tags_to_alert_drpdwn", "value"),
    Output(f"{SETUP.ROUTE}_slack_drpdwn", "value"),
    Output(f"{SETUP.ROUTE}_alert_input", "value"),
    Input("redirect", "pathname"),
    Input(f"{SETUP.ROUTE}_refresh", "data"),
)
def initial_form_fill_callback(_1, _2):
    return None, *fetch_data()


@dash.callback(
    Output(f"{SETUP.ROUTE}_msg", "children"),
    Output(f"{SETUP.ROUTE}_refresh", "data"),
    Input(f"{SETUP.ROUTE}_save_btn", "n_clicks"),
    State(f"{SETUP.ROUTE}_tags_input", "value"),
    State(f"{SETUP.ROUTE}_tags_to_delete", "value"),
    State(f"{SETUP.ROUTE}_tags_to_alert_drpdwn", "value"),
    State(f"{SETUP.ROUTE}_tags_to_alert_drpdwn", "data"),
    State(f"{SETUP.ROUTE}_slack_drpdwn", "value"),
    State(f"{SETUP.ROUTE}_alert_input", "value"),
    prevent_initial_call=True,
)
def save_callback(
    n_clicks,
    new_tags,
    tags_to_delete,
    tags_to_alert,
    all_tags,
    users,
    alert_percent,
):
    if n_clicks:
        return update_data(
            users,
            new_tags,
            tags_to_delete,
            tags_to_alert,
            all_tags,
            alert_percent,
        )
    raise PreventUpdate
