import dash_mantine_components as dmc


def dropdown(
    id,
    options=[],
    value=None,
    placeholder="Select",
    style={},
    persistence=True,
    searchable=True,
    allow_deselect=False,
    small=False,
    **kwargs
):
    _class = "dropdown"
    if small:
        _class += " small"
    return dmc.Select(
        id=id,
        data=options,
        value=value,
        allowDeselect=allow_deselect,
        searchable=searchable,
        placeholder=placeholder,
        style=style,
        className=_class,
        persistence=persistence,
        **kwargs,
    )
