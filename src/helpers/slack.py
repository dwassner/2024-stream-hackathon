from slack_sdk.errors import SlackApiError
import pandas as pd
import slack_sdk
import traceback
import os

THROTTLING_RESPONSE = 429


def create_connection():
    return slack_sdk.WebClient(token=os.getenv("slack_key"))


def process_response(func, **kwargs):
    try:
        return func(**kwargs)
    except SlackApiError as e:
        if e.response.status_code == THROTTLING_RESPONSE:
            delay = int(e.response.headers["Retry-After"])
            print(f"slack throttled for {delay} seconds")
            return f"Slack API is currently busy, try again in roughly {delay} seconds"
        else:
            traceback.print_exc()
            return str(e)


def get_slack_users_df():
    client = create_connection()
    r = process_response(client.users_list)
    if isinstance(r, str):
        return r
    return pd.DataFrame(r["members"])


def dummy_names():
    return ["Dustin Wassner", "Umesh Pathak"]


def create_list_of_active_slack_usersnames():
    return dummy_names()
    df = get_slack_users_df()
    if isinstance(df, str):
        return df
    df = df.loc[(df["real_name"].notna()) & (df["is_bot"] == False)]
    df = df.sort_values(by=["real_name"])
    return df["real_name"].values.tolist()


def create_dict_of_active_slack_users():
    df = get_slack_users_df()
    if isinstance(df, str):
        return df
    return df.set_index("real_name")["id"].to_dict()


def send_slack_dm(user_id, message):
    print(user_id, message)
    client = create_connection()
    process_response(client.chat_postMessage, channel=user_id, text=message)
