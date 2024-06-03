import string
import random
import traceback

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text

from config import rds_creds

MAX_LOCK_WAIT = 500


def get_connection_url(
    user=rds_creds.user,
    pw=rds_creds.pw,
    host=rds_creds.host,
    port=rds_creds.port,
    db=rds_creds.db,
):
    return f"mysql+pymysql://{user}:{pw}@{host}:{port}/{db}"


def create_connection():
    print("creating connection")
    url = get_connection_url()
    args = {"init_command": f"SET SESSION innodb_lock_wait_timeout={MAX_LOCK_WAIT}"}
    try:
        return create_engine(url, connect_args=args)
    except Exception as ex:
        error = f"Database connection fail; Error: {ex}"
        return error


def db_to_df(query, engine=None):
    try:
        if not engine:
            engine = create_connection()
        with engine.begin() as conn:
            df = pd.read_sql(text(query), conn)
            return df, False
    except Exception as e:
        traceback.print_exc()
        return f"Error: {e}", True


def upsert_df(df, tbl, no_update=[], engine=None, batch_size=10_000):
    try:
        if not engine:
            engine = create_connection()
        df = df.replace({np.nan: None})

        cols = ", ".join(df.columns)
        placeholders = ", ".join([":" + col for col in df.columns])
        sql_upsert = f"""
            INSERT INTO {tbl} ({cols})
            VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE
        """
        if len(no_update) > 0:
            df = df.drop(columns=no_update)
        update_stmt = ", ".join(
            [
                f"{col} = IF(LOWER(VALUES({col}))='null', NULL, VALUES({col}))"
                for col in df.columns
                if col not in no_update
            ]
        )
        sql_upsert += update_stmt

        with engine.begin() as conn:
            for start_row in range(0, df.shape[0], batch_size):
                end_row = min(start_row + batch_size, df.shape[0])
                batch_df = df.iloc[start_row:end_row]
                conn.execute(text(sql_upsert), batch_df.to_dict(orient="records"))

        return True, None
    except Exception as e:
        traceback.print_exc()
        return False, e


def execute_sql(stmt, db_res=False, engine=None):
    try:
        if not engine:
            engine = create_connection()
        with engine.begin() as conn:
            r = conn.execute(text(stmt))
            if db_res:
                return r, None
            return True, None
    except Exception as e:
        traceback.print_exc()
        return False, e
