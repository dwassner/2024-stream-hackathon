from datetime import datetime, timedelta


def get_date_range(preset, offset=2):
    max_date = datetime.now() - timedelta(days=offset)
    min_date = max_date - timedelta(days=int(preset))
    return [dt.strftime("%Y-%m-%d") for dt in [min_date, max_date]]


def get_prior_date_range(date_range):
    start_dt = datetime.strptime(date_range[0], "%Y-%m-%d")
    end_dt = datetime.strptime(date_range[1], "%Y-%m-%d")
    end_str = (start_dt - timedelta(days=1)).strftime("%Y-%m-%d")
    start_str = (start_dt - timedelta(days=1) - (end_dt - start_dt)).strftime(
        "%Y-%m-%d"
    )
    return [start_str, end_str]
