import dash_ag_grid as dag
import numpy as np


def define_column_settings(header_class):
    settings = {
        "filter": False,
        "resizable": True,
        "sortable": True,
        "editable": False,
        "floatingFilter": True,
        "cellDataType": False,
    }
    if header_class:
        settings.update({"headerClass": {"function": f"{header_class}(params)"}})
    return settings


def define_grid_options(
    pagination, suppress_col_virtualisation, custom_no_rows_msg, pinned_bottom_rows
):
    options = {
        "animateRows": True,
        "enableCellTextSelection": True,
        "undoRedoCellEditing": True,
        "rowSelection": "single",
        "pagination": pagination,
        "paginationPageSize": 50,
        "stopEditingWhenCellsLoseFocus": True,
        "rowHeight": 40,
        "suppressColumnVirtualisation": suppress_col_virtualisation,
        "tooltipShowDelay": 0,
    }
    if custom_no_rows_msg:
        options.update(
            {
                "noRowsOverlayComponent": "CustomNoRowsOverlay",
                "noRowsOverlayComponentParams": {
                    "message": custom_no_rows_msg,
                    "fontSize": 20,
                },
            }
        )

    if pinned_bottom_rows:
        options.update({"pinnedBottomRowData": pinned_bottom_rows})
    return options


def update_col_widths(col_size_opts):
    values = [
        {"key": key.DB if not isinstance(key, str) else key, "minWidth": width}
        for key, width in col_size_opts.items()
    ]
    return {"columnLimits": values}


def set_custom_sorting(cols, currency_cols, percent_cols, comma_cols):
    cols_to_sort = currency_cols + percent_cols + comma_cols
    for col_setting in cols:
        if col_setting["field"] in cols_to_sort:
            col_setting.update({"comparator": {"function": "comparator"}})


def currency_conversion(x, no_truncate):
    suffix = ""
    if not no_truncate:
        if float(x) > 1000:
            x = float(x) / 1000
            suffix = "K"
        return f"${x:,.2f}{suffix}" if (x and not np.isnan(x)) else "N/A"
    if x and not np.isnan(x):
        if isinstance(x, float):
            return f"${float(x):,.2f}"
        return f"${int(x):,}"
    return "N/A"


def percent_conversion(x):
    return f"{x * 100 :,.1f}%" if x else "N/A"


def comma_conversion(x):
    return f"{int(x):,}"


def format_values(df, currency_cols, percent_cols, comma_cols, no_truncate_cols):
    if df.empty:
        return df
    func_maps = {
        currency_conversion: currency_cols,
        percent_conversion: percent_cols,
        comma_conversion: comma_cols,
    }
    for func, cols in func_maps.items():
        for col in cols:
            if col not in df:
                continue
            try:
                if func == currency_conversion:
                    no_truncate = col in no_truncate_cols
                    df[col] = df[col].apply(func, args=(no_truncate,))
                else:
                    df[col] = df[col].apply(func)
            except Exception:
                continue
    return df


def create_ag_grid(
    df,
    id_prefix,
    cols,
    col_size_opts=None,
    height="700px",
    pagination=None,
    enable_pagination=True,
    export=None,
    col_size="responsiveSizeToFit",
    suppress_col_virtualisation=False,
    margin="auto",
    class_name="ag-theme-alpine compact",
    width=None,
    currency_cols=[],
    no_truncate_cols=[],
    percent_cols=[],
    comma_cols=[],
    custom_no_rows_msg=None,
    pinned_bottom_rows=[],
    header_class=None,
):
    options = define_grid_options(
        enable_pagination,
        suppress_col_virtualisation,
        custom_no_rows_msg,
        pinned_bottom_rows,
    )
    if width:
        style = {"height": height, "margin": margin, "width": width}
    else:
        style = {"height": height, "margin": margin}
    grid_id = f"{id_prefix}_grid"

    if any([currency_cols, percent_cols, comma_cols]):
        set_custom_sorting(cols, currency_cols, percent_cols, comma_cols)
        df = format_values(
            df, currency_cols, percent_cols, comma_cols, no_truncate_cols
        )

    grid = dag.AgGrid(
        id=grid_id,
        className=class_name,
        columnDefs=cols,
        rowData=df.to_dict("records"),
        columnSize=col_size,
        defaultColDef=define_column_settings(header_class),
        dashGridOptions=options,
        style=style,
    )

    if col_size_opts:
        grid.columnSizeOptions = update_col_widths(col_size_opts)
    if pagination:
        grid.dashGridOptions["paginationPageSize"] = pagination
    if export:
        grid.csvExportParams = {"fileName": export}
    return grid
