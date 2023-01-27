from load_csv import load_csv
from time_manager import TimeManager
from generate_players import generate_initial_players
from team import Team
from country import Country
from contract_manager import ContractManager
from datetime import datetime
from champutils import ChampUtils
from generate_calendar import generate_all_calendars
from championship import Championship
from match import Match
from mercato import mercato
from os import path, makedirs

contract_manager = ContractManager()


def main():
    if not path.exists("data-test"):
        makedirs("data-test")
    matches_csv = open("data-test/matches.csv", "w")
    matches_csv.write("id_championnat;date_debut;club_dom;club_ext;score_dom;score_ext;gagnant;tnc_dom;tnc_ext;tc_dom;tc_ext;points_dom;points_ext;id_commune\n")
    players_csv = open("data-test/players.csv", "w")
    players_csv.write("id_joueur;nom;prenom;date_naissance;id_nationalite;poste\n")
    b = open("data-test/champutils.txt", "w")
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
        teams.append(Team(team["id_club"], team["id_championnat"], championships, team["id_commune"]))
        teams_per_championships[team["id_championnat"]].append(int(team["id_club"]))
    players_number = 0
    time_manager = TimeManager()
    teams_per_championship = dict()
    teams_per_id = dict()
    for team in teams:
        teams_per_championship[int(team.get_id_club())] = int(team.get_id_championship())
        teams_per_id[int(team.get_id_club())] = team
        generated_players = generate_initial_players(players_csv, time_manager.date, team, nationalities_countries)
        for player in generated_players:
            contract_manager.add_contract(player.get_id(), team.get_id_club(), datetime(1970, 1, 1))
        team.add_players(generated_players)
        players_number += team.get_amount_players()

    champ_utils = ChampUtils()
    # TODO systeme d'année et champutils
    matches = generate_all_calendars(teams_per_championships)
    i = 0
    while time_manager.get_date() < datetime(2080, 9, 1):
        if time_manager.mercato_time():
            mercato(players_csv, championships, players_number, teams_per_championships, time_manager.get_date(), contract_manager, teams_per_id, nationalities_countries)
            time_manager.skip_mercato_time()
        elif time_manager.is_season_finished():
            b.write(f"{time_manager.get_date().year} = {str(champ_utils)}\n")
            winners = champ_utils.close()
            b.write(f"Winner {time_manager.get_date().year} = {winners}\n")
            matches = generate_all_calendars(teams_per_championships)
            time_manager.add_day()
        else:
            for match in matches[i]:
                team1 = teams_per_id[match[0]]
                commune_match = team1.get_commune_id()
                match_object = Match(teams_per_championship[match[0]], time_manager.get_date(), teams_per_id[match[0]], teams_per_id[match[1]], commune_match)
                match_object.simulate(champ_utils)
                matches_csv.write(f"{match_object.to_csv()}\n")
            time_manager.add_day()
            if i != 189:
                i += 1
            else:
                i = 0
    matches_csv.close()
    players_csv.close()
    b.close()

    return  # nb de joueurs par équipe : 22-25 pour EN et ES, 22-36 sinon


if __name__ == '__main__':
    main()
