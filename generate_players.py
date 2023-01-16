from team import Team
from random import randint


NUMBER_OF_PLAYERS_PER_COUNTRY = {
    "155": {
        'G': 3,
        'D': 10,
        'M': 7,
        'A': 2
    },
    "55": {
        'G': 3,
        'D': 10,
        'M': 7,
        'A': 2
    },
    "64": {
        'G': 3,
        'D': 10,
        'M': 7,
        'A': 2
    }
}


def generate_players(team: Team) -> list:
    number_of_players = NUMBER_OF_PLAYERS_PER_COUNTRY[team.championship.country.id_country]
    return []
