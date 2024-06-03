import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

from src.layout_components.loading_overlay import loading_overlay
from src.layout_components.dropdown import dropdown
from src.layout_components.button import button
from src.routing import BUDGET


def create_banner():
    return html.H1("Budgets", className="page-heading")


def create_msg_div():
    return html.H5(
        "Please wait...",
        id=f"{BUDGET.ROUTE}_msg",
        className="message",
        style={"text-align": "left"},
    )


def table_div():
    return html.Div(
        id=f"{BUDGET.ROUTE}_table",
        children=html.Div(id=f"{BUDGET.ROUTE}_grid"),
        style={"height": "700px"},
    )


def create_tags_input_div():
    id = f"{BUDGET.ROUTE}_tags_input"
    label = html.H5("Select Tag:", style={"width": "130px"})
    drpdown = dropdown(id, persistence=False)
    return dmc.Group([label, drpdown])


def top_div():
    tags_input = create_tags_input_div()
    apply_btn = button("Apply", f"{BUDGET.ROUTE}_apply_button")
    return dbc.Stack(
        dmc.Group([tags_input, apply_btn]), className="left-stack primary top"
    )


def create_main_body():
    return dbc.Stack(
        [
            create_banner(),
            create_msg_div(),
            top_div(),
            dmc.Space(h="xl"),
            loading_overlay(
                [
                    dcc.Store(id=f"{BUDGET.ROUTE}_refresh_data"),
                    table_div(),
                ]
            ),
        ],
        class_name="main-body",
    )


def layout():
    body = dbc.Container([create_main_body()], class_name="container-main")
    return dbc.Container([body], fluid=True)
