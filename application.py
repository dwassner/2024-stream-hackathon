from dash_bootstrap_components.themes import BOOTSTRAP
from dash import Dash

from src.constants import HIGHCHARTS, HIGHMAPS, DANFOJS
from src.helpers.flask_login import server
from src import main_container

app = Dash(
    __name__,
    server=server,
    use_pages=True,
    pages_folder="src/pages",
    suppress_callback_exceptions=True,
    external_stylesheets=[BOOTSTRAP],
    external_scripts=[HIGHMAPS, HIGHCHARTS, DANFOJS],
)
app.layout = main_container.layout()

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
