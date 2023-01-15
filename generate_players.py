from team import Team
from random import randint


def generate_players(team: Team) -> list:
    if team.championship.country.id_country == '155' or team.championship.country.id_country == '55':
        number_of_players = randint(22, 25)
    else:
        number_of_players = randint(22, 36)
    #
    return []
