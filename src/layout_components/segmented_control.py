import dash_mantine_components as dmc


def segmented_control(id, options=[], value=None, small=True):
    if small:
        _class = "small"
        size = "xs"
    else:
        _class = None
        size = "md"
    return dmc.SegmentedControl(
        id=id, data=options, value=value, size=size, radius=30, className=_class
    )
