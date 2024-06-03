from .button import button


def button_clear_filters(id):
    return button("Clear Filters", id, small=True, outlined=True)
