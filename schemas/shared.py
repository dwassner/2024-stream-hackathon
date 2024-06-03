from collections import namedtuple
from dataclasses import dataclass


@dataclass
class Shared:
    COLS = namedtuple("COLS", ("DB", "DISP"))
    MARKETPLACE_ID = COLS("marketplace_id", "Marketplace Id")
    PROFILE_ID = COLS("profile_id", "Profile ID")

    FLIGHT_ID = COLS("flight_id", "Flight ID")
    ORDER_ID = COLS("order_id", "Order ID")
    LINE_ITEM_ID = COLS("line_item_id", "Line Item ID")

    PORTFOLIO_ID = COLS("portfolio_id", "Portfolio ID")
    CAMPAIGN_ID = COLS("campaign_id", "Campaign ID")
    AD_GROUP_ID = COLS("ad_group_id", "Ad Group ID")
    AD_ID = COLS("ad_id", "Ad ID")
    KEYWORD_ID = COLS("keyword_id", "Keyword ID")
    TARGET_ID = COLS("target_id", "Target ID")

    NAME = COLS("name", "Name")
    CAMPAIGN_NAME = COLS("campaign_name", "Campaign Name")
    AD_GROUP_NAME = COLS("ad_group_name", "Ad Group Name")

    KEYWORD_TEXT = COLS("keyword_text", "Keyword Text")
    KEYWORDS = COLS("keywords", "Keywords")

    PLACEMENT = COLS("placement", "Placement")
    AD_TYPE = COLS("ad_type", "Ad Type")
    REPORT_TYPE = COLS("report_type", "Report Type")
    MATCH_TYPE = COLS("match_type", "Match Type")

    STATE = COLS("state", "State")
    SERVING_STATUS = COLS("serving_status", "Serving Status")

    PSR_GROUP = COLS("psr_group", "PSR Group")
    BRAND = COLS("brand", "Brand")

    PARENT_ASIN = COLS("parent_asin", "Parent ASIN")
    CHILD_ASIN = COLS("child_asin", "Child ASIN")
    SKU = COLS("sku", "SKU")

    SESSIONS = COLS("sessions", "Sessions")
    IMPRESSIONS = COLS("impressions", "Impressions")
    CLICKS = COLS("clicks", "Clicks")
    SPEND = COLS("spend", "Spend")
    COST = COLS("cost", "Cost")

    SALES = COLS("ad_sales", "Ad Sales")
    TOTAL_SALES = COLS("total_sales", "Total Sales")
    ORDERS = COLS("ad_orders", "Ad Orders")
    TOTAL_ORDERS = COLS("total_orders", "Total Orders")

    TARGET_ACOS = COLS("target_acos", "Target ACOS")
    AOV = COLS("aov", "AOV")

    CREATION_DATE = COLS("creation_date", "Creation Date")
    START_DATE = COLS("start_date", "Start Date")
    END_DATE = COLS("end_date", "End Date")

    DATE = COLS("date", "Date")
    HOUR = COLS("hour", "Hour")
    DATE_ADDED = COLS("date_added", "Date Added")
    TIME_ADDED = COLS("time_added", "Time Added")
    LAST_UPDATED_IN_DB = COLS("last_updated_in_db", "Last Updated In DB")

    ORIGIN = COLS("origin", "Origin")

    SEED_KEYWORD = COLS("seed_kw", "Seed Keyword")
