import pandas as pd
import dash

from src.layout_components.ag_grid import create_ag_grid
from src.constants import MiscCols
from src.routing import PLACEMENTS
from src.helpers import db_funcs

from schemas.shared import Shared
from schemas.conversion import ConversionTable
from schemas.traffic import TrafficTable


def get_traffic_df(dates):
    query = f"""
        SELECT
            t.{Shared.PLACEMENT.DB},
            t.{TrafficTable.TIME_WINDOW_START.DB},
            SUM(t.{Shared.CLICKS.DB}) AS {Shared.CLICKS.DB},
            SUM(t.{Shared.SPEND.DB}) AS {Shared.SPEND.DB},
            SUM(c.{Shared.ORDERS.DB}) AS {Shared.ORDERS.DB},
            SUM(c.{Shared.SALES.DB}) AS {Shared.SALES.DB}
        FROM brand_a_{TrafficTable.TABLE_NAME} as t
        LEFT JOIN brand_a_{ConversionTable.TABLE_NAME} as c
            ON t.{Shared.CAMPAIGN_ID.DB} = c.{Shared.CAMPAIGN_ID.DB}
        WHERE
            t.{TrafficTable.TIME_WINDOW_START.DB} BETWEEN '{dates[0]}' AND '{dates[1]}'
            AND t.{Shared.PLACEMENT.DB} IS NOT NULL
        GROUP BY {Shared.PLACEMENT.DB}, t.{TrafficTable.TIME_WINDOW_START.DB}
    """
    df, e = db_funcs.db_to_df(query)
    if e:
        return e
    return df


def get_cols():
    cols = {
        Shared.PLACEMENT: 200,
        Shared.CLICKS: 130,
        Shared.SPEND: 130,
        Shared.ORDERS: 130,
        Shared.SALES: 130,
    }
    cols.update(misc_cols())
    return cols


def misc_cols():
    return {MiscCols.CPC: 75, MiscCols.CVR: 75}


def group_and_add_misc_cols(df, grouper):
    agg_cols = [Shared.CLICKS, Shared.SPEND, Shared.ORDERS, Shared.SALES]
    aggs = {col.DB: "sum" for col in agg_cols}
    df = df.groupby(grouper).agg(aggs).reset_index()
    df = add_misc_cols(df)
    return df


def add_misc_cols(df):
    if df.empty:
        return df
    extra_cols = list(misc_cols().keys())
    df[extra_cols] = df.apply(calculate_misc_col_values, axis=1, result_type="expand")
    df = df.fillna(0)
    return df


def calculate_misc_col_values(row):
    if not row[Shared.CLICKS.DB]:
        return [0, 0]

    cpc = row[Shared.SPEND.DB] / row[Shared.CLICKS.DB]
    cvr = row[Shared.ORDERS.DB] / row[Shared.CLICKS.DB]
    return [cpc, cvr]


def currency_cols():
    return [Shared.SPEND, Shared.SALES, MiscCols.CPC]


def percent_cols():
    return [MiscCols.CVR]


def comma_cols():
    return [Shared.CLICKS, Shared.ORDERS]


def custom_formatters(col):
    formatters = {
        "comma_cols": "params.value.toLocaleString()",
        "percent_cols": "percentFormat(params, 1)",
        "currency_cols": "currencyFormat(params, '$', 2)",
    }
    return formatters[col]


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
        if col in comma_cols():
            specs.update(
                {"valueFormatter": {"function": custom_formatters("comma_cols")}}
            )
        if col in currency_cols():
            specs.update(
                {"valueFormatter": {"function": custom_formatters("currency_cols")}}
            )
        if col in percent_cols():
            specs.update(
                {"valueFormatter": {"function": custom_formatters("percent_cols")}}
            )
        if col == Shared.PLACEMENT:
            specs.update({"cellStyle": {"textAlign": "left"}})
        col_settings.append(specs)
    return col_settings


def prepare_spline_data(rows, placements, col, base_entry):
    placement_col = Shared.PLACEMENT.DB
    spline_data = []
    for index, placement in enumerate(placements):
        if col in [Shared.SPEND.DB, Shared.SALES.DB, MiscCols.CPC]:
            data = [
                float(f"{r[col]:.2f}") for r in rows if r[placement_col] == placement
            ]
        else:
            data = [
                float(f"{r[col] * 100:.2f}")
                for r in rows
                if r[placement_col] == placement
            ]
        entry = {**base_entry, "type": "spline", "name": placement, "data": data}
        if index != 0:
            entry.update({"linkedTo": ":previous"})
        spline_data.append(entry)
    return spline_data


def prepare_charts_data(df):
    date_col = TrafficTable.TIME_WINDOW_START.DB
    df[date_col] = df[date_col].apply(lambda x: x.date())
    df = group_and_add_misc_cols(df, [date_col, Shared.PLACEMENT.DB])
    df = df.sort_values(by=[date_col])
    dates = sorted(df[date_col].unique().tolist())
    categories = [d.strftime("%b %d, %Y") for d in dates]
    placements = sorted(df[Shared.PLACEMENT.DB].unique().tolist())

    spend_dict = {"legendName": "Spend", "visible": False}

    sales_dict = {
        "legendName": "Ad Sales",
        "yAxis": 1,
        "tooltip": {"valuePrefix": " $"},
    }

    cpc_dict = {
        "legendName": "CPC",
        "yAxis": 2,
        "tooltip": {"valuePrefix": "$"},
    }

    cvr_dict = {
        "legendName": "CVR",
        "yAxis": 3,
        "tooltip": {"valueSuffix": " %"},
    }

    rows = df.to_dict(orient="records")
    data = [
        *prepare_spline_data(rows, placements, Shared.SPEND.DB, spend_dict),
        *prepare_spline_data(rows, placements, Shared.SALES.DB, sales_dict),
        *prepare_spline_data(rows, placements, MiscCols.CPC, cpc_dict),
        *prepare_spline_data(rows, placements, MiscCols.CVR, cvr_dict),
    ]
    return {"data": data, "categories": categories}


def get_data(dates):
    df = get_traffic_df(dates)
    table_df = group_and_add_misc_cols(df, [Shared.PLACEMENT.DB])
    cols = define_col_settings()
    grid = create_ag_grid(table_df, PLACEMENTS.ROUTE, cols, col_size_opts=get_cols())
    chart_data = prepare_charts_data(df)
    return chart_data, grid
