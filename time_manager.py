from datetime import datetime, timedelta


class TimeManager:
    def __init__(self, day: int = 8, month: int = 1, year: int = 1970) -> None:
        self.date: datetime = datetime(year, month, day)

    def mercato_time(self) -> bool:
        winter_mercato = datetime(self.date.year - 1, 12, 15) <= self.date <= datetime(self.date.year, 1, 7)
        summer_mercato = datetime(self.date.year, 7, 1) <= self.date <= datetime(self.date.year, 8, 31)
        return winter_mercato or summer_mercato

    def match_time(self) -> bool:
        return not (self.mercato_time())

    def skip_mercato_time(self):
        if self.match_time():
            return
        current_year = self.date.year
        if self.date.month == 12 or self.date.month == 1:
            self.date = datetime(8,  1, current_year+1)
        else:
            self.date = datetime(31, 8, current_year)

    def add_day(self):
        self.date += timedelta(days=1)

    def __str__(self) -> str:  # French way of displaying date
        return self.date.strftime("%d/%m/%Y")