from load_csv import load_csv
from time_manager import TimeManager
from generate_players import generate_players
from team import Team
from country import Country
from contract_manager import ContractManager
from datetime import datetime
from champutils import ChampUtils
from generate_calendar import generate_all_calendars
from championship import Championship
from match import Match
from mercato import mercato

contract_manager = ContractManager()


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
        teams.append(Team(team["id_club"], team["id_championnat"], championships, 99))
        teams_per_championships[team["id_championnat"]].append(i)
    players_number = 0
    time_manager = TimeManager()
    for team in teams:
        generate_players(time_manager.date, team, nationalities_countries)
        players_number += team.get_amount_players()

    champ_utils = ChampUtils()
    # TODO systeme d'année et champutils
    matches = generate_all_calendars(teams_per_championships)
    i = 0
    while time_manager.get_date() < datetime(2080, 9, 1):
        if time_manager.mercato_time():
            mercato(championships, players_number, teams_per_championships)
            time_manager.skip_mercato_time()
        elif time_manager.is_season_finished:
            champ_utils.close()
            matches_per_championship = generate_all_calendars(teams_per_championships)
            time_manager.add_day()
        else:
            for match in matches[i]:
                match_object = Match(match[2], time_manager.get_date(), match[0], match[1])
                match_object.simulate(champ_utils)
            time_manager.add_day()
            i += 1
    return  # nb de joueurs par équipe : 22-25 pour EN et ES, 22-36 sinon


def get_contract_manager():
    return contract_manager


if __name__ == '__main__':
    main()
