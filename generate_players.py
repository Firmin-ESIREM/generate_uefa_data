from team import Team
from random import randint, choice
from datetime import datetime
from dateutil.relativedelta import relativedelta
from country import Country
from player import Player


def generate_players(date: datetime, team: Team, countries: list[Country]) -> list[Player]:
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
    for post, player in number_of_players_per_post.items():
        low = round(datetime.timestamp(date - relativedelta(years=35)))
        up = round(datetime.timestamp(date - relativedelta(years=17)))
        birth_date = datetime.fromtimestamp(randint(low, up))
        nationality = team.championship.country.id_nationality if bool(randint(0, 1)) else choice(countries).id_nationality
        player = Player(team, nationality, birth_date, post)
        players.append(Player(team, nationality, birth_date, post))
    return []
