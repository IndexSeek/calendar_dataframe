import calendf
import pandas as pd


def test_min_start_date():
    df = calendf.create_calendar_df(start_date="2020-01-01", end_date="2023-12-31")
    assert min(df.date) == pd.Timestamp("2020-01-01")


def test_max_end_date():
    df = calendf.create_calendar_df(start_date="2020-01-01", end_date="2023-12-31")
    assert max(df.date) == pd.Timestamp("2023-12-31")
