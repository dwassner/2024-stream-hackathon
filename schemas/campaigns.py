from collections import namedtuple
from dataclasses import dataclass


@dataclass
class TagPrefix:
    TAG = "tag_"


@dataclass
class CampaignsListTable:
    TABLE_NAME = "campaigns"
    COLS = namedtuple("COLS", ("DB", "DISP"))
    NAME = COLS("name", "Campaign Name")
    BUDGET = COLS("budget", "Budget")
    TAG_1 = COLS(f"{TagPrefix.TAG}1", "Tag 1")
    TAG_2 = COLS(f"{TagPrefix.TAG}2", "Tag 2")
    TAG_3 = COLS(f"{TagPrefix.TAG}3", "Tag 3")
    ALL_TAGS = [TAG_1, TAG_2, TAG_3]
