from team import Team
from random import randint, choice
from datetime import datetime
from dateutil.relativedelta import relativedelta
from country import Country
from player import Player
from random_date import random_date


ALL_PLAYERS = []


def generate_player(players_file, date: datetime, countries: list[Country], team: Team, post: str, age_min: int, age_max: int,
                    age_mid: int = None, weight_young: float = 1) -> Player:
    low = date - relativedelta(years=age_max)
    up = date - relativedelta(years=age_min)
    if age_mid is None:
        birth_date = random_date(low, up)
    else:
        mid = date - relativedelta(years=age_mid)
        birth_date = random_date(low, mid) if randint(1, 100) > weight_young * 100 else random_date(mid, up)
    nationality = team.championship.country.id_nationality if bool(randint(0, 1)) else choice(countries).id_nationality
    player_generated = Player(team, nationality, birth_date, post)
    ALL_PLAYERS.append(player_generated)
    players_file.write(f"{player_generated.id};{player_generated.last_name};{player_generated.first_name};{birth_date.year}-{birth_date.month}-{birth_date.day};{nationality};{post}\n")
    return player_generated


def generate_initial_players(players_file, date: datetime, team: Team, countries: list[Country], post=None) -> list[Player]:
    if team.championship.country.id_country == '155' or team.championship.country.id_country == '55':
        max_number_of_players = 25
    else:
        max_number_of_players = 36
    number_of_players_per_post = {
        'G': randint(2, 3),
        'D': randint(8, 10),
        'M': randint(6, 9),
        'A': randint(2, 7)
    }
    while sum(number_of_players_per_post.values()) > max_number_of_players:
        i = []
        if number_of_players_per_post['G'] > 3:
            i.append('G')
        if number_of_players_per_post['D'] > 8:
            i.append('D')
        if number_of_players_per_post['M'] > 6:
            i.append('M')
        if number_of_players_per_post['A'] > 2:
            i.append('A')
        to_remove = choice(i)
        number_of_players_per_post[to_remove] -= 1
    players: list[Player] = []
    for post, number_of_players in number_of_players_per_post.items():
        for _ in range(number_of_players):
            """low = date - relativedelta(years=35)
            up = date - relativedelta(years=17)
            birth_date = random_date(low, up)
            nationality = team.championship.country.id_nationality if bool(randint(0, 1)) else choice(
                countries).id_nationality
            player_generated = Player(team, nationality, birth_date, post)"""
            player_generated = generate_player(players_file, date, countries, team, post, 17, 35)
            players.append(player_generated)
    return players
