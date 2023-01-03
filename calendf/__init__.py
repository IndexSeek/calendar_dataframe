import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar


def create_calendar_df(start_date, end_date):
    dates_df = pd.DataFrame(
        pd.date_range(start=start_date, end=end_date), columns=["date"]
    )

    holiday_df = (
        USFederalHolidayCalendar()
        .holidays(start=start_date, end=end_date, return_name=True)
        .reset_index(name="holiday")
        .rename(columns={"index": "date"})
    )

    df = dates_df.join(holiday_df.set_index("date"), on="date")

    return df
