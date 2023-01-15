from country import Country


class Championship:
    def __init__(self, id_championship: str, id_country: str, countries: list[Country]):
        self.id_championship: str = id_championship
        self.country: Country = next((x for x in countries if x.id_country == id_country), None)

    def get_id(self):
        return self.id_championship