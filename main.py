from load_csv import load_csv
from time_manager import TimeManager
from generate_players import generate_players
from mercato import mercato
from team import Team
from country import Country
from championship import Championship


def main():
    nationalities_countries_dict = load_csv("nationalites_pays")
    nationalities_countries = []
    for nc in nationalities_countries_dict:
        nationalities_countries.append(Country(nc["id_pays"], nc["id_nationalite"]))
    championships_dict = load_csv("championnats")
    championships = []
    teams_per_championships = {}
    for championship in championships_dict:
        championships.append(
            Championship(championship["id_championnat"], championship["id_pays"], nationalities_countries))
        teams_per_championships[championship["id_championnat"]] = list()
    teams_dict = load_csv("teams")
    teams = []
    for i, team in enumerate(teams_dict):
        teams.append(Team(team["id_club"], team["id_championnat"], championships))
        teams_per_championships[team["id_championnat"]].append(i)
    players_number = 0
    for team in teams:
        generate_players(team)
        players_number += team.get_amount_players()
    time_manager = TimeManager()
    if time_manager.mercato_time():
        mercato(championships, players_number, teams_per_championships)
        time_manager.skip_mercato_time()
    else:
        time_manager.add_day()
    return  # nb de joueurs par équipe : 22-25 pour EN et ES, 22-36 sinon


if __name__ == '__main__':
    main()
