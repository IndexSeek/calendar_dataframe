import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar


def create_calendar_df(
    start_date, end_date, holiday_calendar=USFederalHolidayCalendar(), accessors=False
):
    dates_df = pd.DataFrame(
        pd.date_range(start=start_date, end=end_date), columns=["date"]
    )
    """
    Returns a Pandas DataFrame with a date range and optional holiday and date accessors.

    You can create a calendar DataFrame in a number of different ways, as shown in the examples
    below.

    Example 1
        Creating example calendar DataFrame with default parameters:
        >>> import calendf
        >>> calendf.create_calendar_df(start_date="2020-01-01", end_date="2023-12-31")

    Example 2
        Creating example calendar DataFrame with a custom Holiday Calendar:
        >>> import calendf
        >>> import pandas as pd
        >>> from pandas.tseries.offsets import DateOffset
        >>> from pandas.tseries.holiday import (
        ...     Holiday,
        ...     USMemorialDay,
        ...     AbstractHolidayCalendar,
        ...     nearest_workday,
        ...     MO,
        >>> )
        >>> class ExampleCalendar(AbstractHolidayCalendar):
        ...     rules = [
        ...     USMemorialDay,
        ...     Holiday("July 4th", month=7, day=4, observance=nearest_workday),
        ...     Holiday(
        ...         "Columbus Day",
        ...         month=10,
        ...         day=1,
        ...         offset=pd.DateOffset(weekday=MO(2)),
        ...     ),
        >>> ]

        >>> calendf.create_calendar_df(start_date="2020-01-01", end_date="2023-12-31", holiday_calendar=ExampleCalendar())

    Example 3
        Creating example calendar DataFrame with date accessors:
        >>> import calendf
        >>> calendf.create_calendar_df(start_date="2020-01-01", end_date="2023-12-31", accessors=True)
        """

    # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html?highlight=holiday#holidays-holiday-calendars
    holiday_df = (
        holiday_calendar.holidays(start=start_date, end=end_date, return_name=True)
        .reset_index(name="holiday")
        .rename(columns={"index": "date"})
    )

    df = dates_df.join(holiday_df.set_index("date"), on="date")

    if accessors:
        # TODO: Incorporate Business Days?
        # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html?highlight=holiday#dateoffset-objects
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["day"] = df["date"].dt.day
        df["day_of_week"] = df["date"].dt.day_of_week
        df["day_of_year"] = df["date"].dt.day_of_year
        df["week_of_year"] = df["date"].dt.isocalendar().week
        df["quarter"] = df["date"].dt.quarter
        df["is_month_start"] = df["date"].dt.is_month_start
        df["is_month_end"] = df["date"].dt.is_month_end
        df["is_quarter_start"] = df["date"].dt.is_quarter_start
        df["is_quarter_end"] = df["date"].dt.is_quarter_end
        df["is_year_start"] = df["date"].dt.is_year_start
        df["is_year_end"] = df["date"].dt.is_year_end
        df["is_leap_year"] = df["date"].dt.is_leap_year

    return df
