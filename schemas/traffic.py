from collections import namedtuple
from dataclasses import dataclass


@dataclass
class TrafficTable:
    COLS = namedtuple("COLS", ("DB", "DISP"))
    TABLE_NAME = "traffic"
    IDEMPOTENCY_ID = COLS("idempotency_id", "Idempotency Id")
    TIME_WINDOW_START = COLS("time_window_start", "Time Window Start")
