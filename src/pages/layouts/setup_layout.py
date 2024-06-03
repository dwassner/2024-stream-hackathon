from datetime import datetime, timedelta
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

from src.layout_components.loading_overlay import loading_overlay
from src.layout_components.multi_select import multi_select
from src.constants import StrategyTypes, Origin
from src.layout_components.button import button
from src.layout_components.input import input
from src.routing import SETUP


def create_banner():
    return html.H1("Setup", className="page-heading")


def create_msg_div():
    return html.H5(id=f"{SETUP.ROUTE}_msg", className="message")


def table_div():
    return html.Div(id=f"{SETUP.ROUTE}_table", style={"height": "700px"})


def create_tags_input():
    id = f"{SETUP.ROUTE}_tags_input"
    style = {"width": "275px"}
    box = input(
        id=id,
        placeholder="For multiple tags, use comma separation",
        style={"width": "350px"},
    )
    return dmc.Group([html.H5("Create tags:", style=style), box])


def delete_tags_dropdown():
    id = f"{SETUP.ROUTE}_tags_to_delete"
    style = {"width": "275px"}
    return dmc.Group(
        [
            html.H5("Remove tags:", style=style),
            multi_select(
                id,
                options=[Origin.BTRMEDIA, Origin.NOT_BTRMEDIA],
                _class="multi-select controls",
                placeholder="Select tags:",
            ),
        ]
    )


def create_send_alerts_dropdown():
    id = f"{SETUP.ROUTE}_tags_to_alert_drpdwn"
    style = {"width": "275px"}
    return dmc.Group(
        [
            html.H5("Send budget alerts for:", style=style),
            multi_select(
                id,
                options=StrategyTypes.ALL,
                _class="multi-select controls",
                placeholder="Select tags:",
            ),
        ]
    )


def create_slack_users_dropdown():
    style = {"width": "275px"}
    id = f"{SETUP.ROUTE}_slack_drpdwn"
    return dmc.Group(
        [
            html.H5("Slack users to receive alerts:", style=style),
            multi_select(
                id,
                _class="multi-select controls",
                placeholder="Select users:",
            ),
        ]
    )


def create_alert_input():
    style = {"width": "275px"}
    box = input(id=f"{SETUP.ROUTE}_alert_input", type="number", value=80)
    return dmc.Group([html.H5("Send Alerts At:", style=style), box, "% of budget used"])


def top_div():
    return dbc.Stack(
        [
            create_msg_div(),
            create_tags_input(),
            dmc.Space(h="lg"),
            delete_tags_dropdown(),
            dmc.Space(h=60),
            create_send_alerts_dropdown(),
            dmc.Space(h="lg"),
            create_slack_users_dropdown(),
            dmc.Space(h="lg"),
            create_alert_input(),
            dmc.Space(h="lg"),
            button("Save", f"{SETUP.ROUTE}_save_btn"),
        ],
        className="left-stack primary top",
    )


def create_main_body():
    return dbc.Stack(
        [
            create_banner(),
            dcc.Store(id=f"{SETUP.ROUTE}_slack_users", storage_type="session"),
            dcc.Store(id=f"{SETUP.ROUTE}_refresh"),
            top_div(),
            dmc.Space(h="xl"),
            loading_overlay([table_div()]),
        ],
        class_name="main-body",
    )


def layout():
    body = dbc.Container([create_main_body()], class_name="container-main")
    return dbc.Container([body], fluid=True)
