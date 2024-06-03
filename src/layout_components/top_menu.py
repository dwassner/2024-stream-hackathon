from dash import html

from src.constants import ImageSourcePaths as Paths
from src import routing


def top_menu_content():
    img = html.Img(src=Paths.COMPANY_LOGO, className="top-menu-img")
    return html.A(img, href=routing.BUDGET.ROUTE)
