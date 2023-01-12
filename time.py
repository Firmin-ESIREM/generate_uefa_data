YEAR_DAYS = {"bissextile": [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
             "not_bissextile": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]}


class TimeManager:
    def __init__(self, day=1, month=1, year=1970):
        self.bissextile = False
        self.month = month
        self.year = year
        self.day = day
        self.is_bissextile()

    def is_bissextile(self):
        self.bissextile = ((self.year % 4 == 0) and (self.year % 100 != 0)) or (self.year % 400 == 0)

    def get_date(self) -> tuple:
        return self.day, self.month, self.year

    def is_month_finished(self):
        bissextile_string = "bissextile" if self.bissextile else "not_bissextile"
        day = YEAR_DAYS[bissextile_string][self.month - 1]
        if self.day > day:
            self.day = 1
            self.month += 1
            self.is_year_finished()
        else:
            return

    def is_year_finished(self):
        if self.month > 12:
            self.month = 1
            self.year += 1
            self.is_bissextile()
        return

    def add_day(self):
        self.day += 1
        self.is_month_finished()

    def is_mercato(self):
        return

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
