from team import Team
from random import randint, choice
from datetime import datetime
from dateutil.relativedelta import relativedelta


def generate_players(date: datetime, team: Team) -> list:
    if team.championship.country.id_country == '155' or team.championship.country.id_country == '55':
        max_number_of_players = 25
    else:
        max_number_of_players = 36
    number_of_players_per_post = {
        'g': randint(2, 3),
        'd': randint(8, 10),
        'm': randint(6, 9),
        'a': randint(2, 7)
    }
    while sum(number_of_players_per_post.values()) > max_number_of_players:
        i = []
        if number_of_players_per_post['g'] > 3:
            i.append('g')
        if number_of_players_per_post['d'] > 8:
            i.append('d')
        if number_of_players_per_post['m'] > 6:
            i.append('m')
        if number_of_players_per_post['a'] > 2:
            i.append('a')
        to_remove = choice(i)
        number_of_players_per_post[to_remove] -= 1
    for post, player in number_of_players_per_post:
        low = round(datetime.timestamp(date - relativedelta(years=35)))
        up = round(datetime.timestamp(date - relativedelta(years=17)))
        birth_date = datetime.fromtimestamp(randint(low, up))

    return []
