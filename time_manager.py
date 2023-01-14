from datetime import datetime


class TimeManager:
    def __init__(self, day: int = 8, month: int = 1, year: int = 1970) -> None:
        self.date: datetime = datetime(year, month, day)

    def mercato_time(self) -> bool:
        winter_mercato = datetime(self.date.year - 1, 12, 15) <= self.date <= datetime(self.date.year, 1, 7)
        summer_mercato = datetime(self.date.year, 7, 1) <= self.date <= datetime(self.date.year, 8, 31)
        return winter_mercato or summer_mercato

    def match_time(self) -> bool:
        return not (self.mercato_time())

    def __str__(self) -> str:  # French way of displaying date
        return self.date.strftime("%d/%m/%Y")
