import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar

dates_df = pd.DataFrame(pd.date_range(start="2015-01-01", end="2023-12-31"), columns=["date"])

holiday_df = (
    USFederalHolidayCalendar()
    .holidays(start="2015-01-01", end="2023-12-31", return_name=True)
    .reset_index(name="holiday")
    .rename(columns={"index": "date"})
)

df = dates_df.join(holiday_df.set_index("date"), on="date")
