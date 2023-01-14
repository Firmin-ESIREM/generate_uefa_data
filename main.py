from load_csv import load_csv
from time_manager import TimeManager
from generate_players import generate_players
from team import Team
from country import Country
from championship import Championship
import random

def mercato(championship_list, players_number: int, teams_per_championship):
    """
    This function permits to "recreate" a mercato.
    """
    numbers_players_to_draft = round(players_number*0.035) # Get the approximatly number of players to need drafts
    for x in numbers_players_to_draft:
        championships = random.choices(championship_list, k=2) # I get two randoms championships
        teams = list() # I create a list for add two randoms teams
        for championship in championships:
            id_champ = championship.get_ip # I get the id of the championship
            teams.append(teams_per_championship[id_champ][random.choice(teams_per_championship[id_champ])]) # I add a random team in this championship
        player1 = random.choice(teams[0].get_players()) # I choose a random player in this team
        player2 = random.choice(teams[1].get_players_per_post(player1.get_post())) # I choose a player with the SAME post in the other team
        teams[0].remove(player1) # I switch players into teams
        teams[1].remove(player2)
        teams[1].add(player1)
        teams[0].add(player2)
        # TODO contracts

def main():
    nationalities_countries_dict = load_csv("nationalites_pays")
    nationalities_countries = []
    for nc in nationalities_countries_dict:
        nationalities_countries.append(Country(nc["id_pays"], nc["id_nationalite"]))
    championships_dict = load_csv("championnats")
    championships = []
    teams_per_championships = {}
    for championship in championships_dict:
        championships.append(Championship(championship["id_championnat"], championship["id_pays"], nationalities_countries))
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
    if (time_manager.mercato_time):
        mercato(championships, players_number, teams_per_championships)
        time_manager.skip_mercato_time()
    else:
        time_manager.add_day()
    return  # nb de joueurs par équipe : 22-25 pour EN et ES, 22-36 sinon


if __name__ == '__main__':
    main()
