import pandas as pd
import dash

from src.constants import MiscCols, StrategyTypes as Strats
from src.layout_components.ag_grid_div import ag_grid_div
from src.layout_components.ag_grid import create_ag_grid
from src.helpers import db_funcs
from src.routing import BUDGET

from schemas.campaigns import CampaignsListTable as Camps
from schemas.alerts_setup import AlertsTable
from schemas.budgets import BudgetsTable
from schemas.shared import Shared


def get_tags():
    query = f"""
        SELECT {AlertsTable.TAGS.DB} FROM {AlertsTable.TABLE_NAME}
        WHERE {Shared.BRAND.DB} = "brand_a"
    """
    df, _ = db_funcs.db_to_df(query)
    if df.empty:
        return Strats.ALL
    tags = df.iloc[0][AlertsTable.TAGS.DB].split(",")
    return tags


def get_data():
    query = f"""
        SELECT
            c.{Shared.CAMPAIGN_ID.DB},
            c.{Camps.NAME.DB},
            b.{BudgetsTable.USAGE_UPDATED_AT.DB},
            c.{Camps.TAG_1.DB},
            b.{BudgetsTable.BUDGET.DB},
            b.{BudgetsTable.BUDGET_USAGE.DB}
        FROM brand_a_{Camps.TABLE_NAME} as c
        LEFT JOIN brand_a_{BudgetsTable.TABLE_NAME} as b
            ON c.{Shared.CAMPAIGN_ID.DB} = b.{BudgetsTable.BUDGET_SCOPE_ID.DB}
        WHERE
            b.{BudgetsTable.BUDGET_SCOPE.DB}="CAMPAIGN"
    """
    df, e = db_funcs.db_to_df(query)
    if e:
        return e
    return df


def get_cols():
    cols = {
        Shared.CAMPAIGN_ID: 10,
        Camps.NAME: 300,
        Camps.TAG_1: 150,
        Camps.BUDGET: 150,
        MiscCols.BUDGET_PERCENT: 200,
    }
    return cols


def define_col_settings():
    col_settings = []
    for col, width in get_cols().items():
        header = col if isinstance(col, str) else col.DISP
        field = col if isinstance(col, str) else col.DB
        specs = {
            "headerName": header,
            "field": field,
            "filter": True,
            "width": width,
            "editable": False,
            "cellStyle": {"textAlign": "center"},
        }
        if col == Camps.TAG_1:
            specs.update({"headerName": "Tag"})
        if col == BudgetsTable.BUDGET:
            specs.update(
                {"valueFormatter": {"function": "currencyFormat(params, '$', 2)"}}
            )
        if col == MiscCols.BUDGET_PERCENT:
            specs.update({"valueFormatter": {"function": "percentFormat(params, 1)"}})
        if col == Camps.NAME:
            specs.update({"cellStyle": {"textAlign": "left"}})
        if col == Shared.CAMPAIGN_ID:
            specs.update({"hide": True, "lockVisible": True})
        col_settings.append(specs)
    return col_settings


def generate_table(filter_model):
    df = get_data()
    df = df.loc[df.groupby(Shared.CAMPAIGN_ID.DB).usage_updated_at.idxmax()]
    df = df.rename(columns={BudgetsTable.BUDGET_USAGE.DB: MiscCols.BUDGET_PERCENT})
    df[MiscCols.BUDGET_PERCENT] = df[MiscCols.BUDGET_PERCENT].apply(lambda x: x / 100)
    cols = define_col_settings()
    id_prefix = BUDGET.ROUTE
    grid = create_ag_grid(df, id_prefix, cols, col_size_opts=get_cols())
    grid.filterModel = filter_model
    tbl = ag_grid_div(grid, id_prefix, undo_btn=False)
    return tbl


def update_table(virtual_row_data, tag_input):
    df = pd.DataFrame(virtual_row_data)
    tag_input = convert_input(tag_input)
    df[Camps.TAG_1.DB] = tag_input
    df = df.filter([Shared.CAMPAIGN_ID.DB, Camps.TAG_1.DB])
    _, e = db_funcs.upsert_df(df, f"brand_a_{Camps.TABLE_NAME}")
    if e:
        return f"Error updating data: {e}", dash.no_update
    return "Successfully Updated", True


def convert_input(tag_input):
    if not tag_input or not tag_input.strip():
        return "NULL"
    return tag_input.strip()
