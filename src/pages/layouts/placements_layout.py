from datetime import datetime, timedelta
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

from src.layout_components.daterange_picker import daterange_picker
from src.layout_components.loading_overlay import loading_overlay
from src.constants import DatePresets
from src.routing import PLACEMENTS


def create_banner():
    return html.H1("Placements", className="page-heading")


def chart_div():
    return html.Div(
        id=f"{PLACEMENTS.ROUTE}_chart", style={"height": "350px"}, className="primary"
    )


def table_div():
    return html.Div(
        id=f"{PLACEMENTS.ROUTE}_table", style={"height": "700px"}, className="primary"
    )


def dt_picker():
    id = f"{PLACEMENTS.ROUTE}_dates"
    max_date = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    return daterange_picker(id, max_date=max_date, presets=DatePresets.RANGE)


def create_main_body():
    return dbc.Stack(
        [
            dcc.Store(id=f"{PLACEMENTS.ROUTE}_data"),
            create_banner(),
            dmc.Space(h="xl"),
            dt_picker(),
            dmc.Space(h="xl"),
            loading_overlay(chart_div()),
            dmc.Space(h="xl"),
            loading_overlay(table_div()),
        ],
        class_name="main-body",
    )


def layout():
    body = dbc.Container([create_main_body()], class_name="container-main")
    return dbc.Container([body], fluid=True)
