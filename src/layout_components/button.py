import dash_mantine_components as dmc


def button(label, id, small=False, preset=False, outlined=False, **extra_kwargs):
    _class = "button"
    if small:
        _class += " small"
    if preset:
        _class += " preset"
    if outlined:
        _class += " outlined"

    kwargs = {"children": label, "id": id, "className": _class}
    kwargs.update(**extra_kwargs)
    return dmc.Button(**kwargs)
