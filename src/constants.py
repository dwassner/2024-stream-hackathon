from dataclasses import dataclass
from collections import namedtuple

@dataclass
class ImageSourcePaths:
    COMPANY_LOGO = "assets/images/logo_color.svg"


@dataclass
class DatePresets:
    RANGE = [7, 14, 30, 60, 90]


@dataclass
class StrategyTypes:
    AUTO = "Auto"
    BRANDED = "Branded"
    EFFICIENCY = "Efficiency"
    AWARENESS = "Awareness"
    RANKING = "Ranking"
    CONQUEST = "Conquest"
    ALL = [AUTO, BRANDED, EFFICIENCY, AWARENESS, RANKING, CONQUEST]


@dataclass
class Origin:
    BTRMEDIA = "BTRMedia"
    NOT_BTRMEDIA = "Non-BTRMedia"


@dataclass
class MiscCols:
    BUDGET_PERCENT = "% of Budget Spent"
    CPC = "CPC"
    CVR = "CVR"

SIDE_MENU = "side-menu"
TOP_MENU = "top-menu"
HIGHCHARTS = "https://code.highcharts.com/highcharts.js"
HIGHMAPS = "https://code.highcharts.com/maps/highmaps.js"
DANFOJS = "https://cdn.jsdelivr.net/npm/danfojs@1.1.2/lib/bundle.min.js"
