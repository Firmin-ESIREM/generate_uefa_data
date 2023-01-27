from random import choice, choices
from datetime import datetime
import json
from generate_players import generate_player
from dateutil import relativedelta


def choices_bibi(liste, k):
    chosen_list = set()
    while len(chosen_list) < k:
        chosen = choice(liste)
        chosen_list.add(chosen)
    tmp = list(chosen_list)
    return tmp
def mercato(championship_list, players_number: int, teams_per_championship, date: datetime, contract_manager,
            teams_per_id, countries):
    """
    This function simulates a transfer market.
    """
    if(date.year != 1970):
        retirement(championship_list, teams_per_championship, date, contract_manager, teams_per_id, countries)
    numbers_players_to_draft = round(players_number * 0.035)  # Get the approximate number of players to need drafts
    for x in range(numbers_players_to_draft):
        championships = choices(championship_list, k=2)  # I get two randoms championships
        teams = list()  # I create a list for add two randoms teams
        for championship in championships:
            id_champ = championship.get_id()  # I get the id of the championship
            teams.append(teams_per_id[choice(teams_per_championship[id_champ])])  # I add a random team in this championship
        player1 = choice(teams[0].get_players())  # I choose a random player in this team
        player2 = choice(
            teams[1].get_players_per_post(player1.get_post()))  # I choose a player with the SAME post in the other team
        teams[0].remove_player(player1)  # I switch players into teams
        teams[1].remove_player(player2)
        teams[1].add_player(player1)
        teams[0].add_player(player2)
        contract_manager.add_contract(player1.get_id(), teams[1].get_id_club(), date)
        contract_manager.add_contract(player2.get_id(), teams[0].get_id_club(), date)



def retirement(championships, teams_per_championship, date, contract_manager, teams_per_id, countries):
    players = list()
    for championship in championships:
        teams = teams_per_championship[championship.get_id()]
        for team1 in teams:
            team = teams_per_id[int(team1)]
            for p in team.get_players():
                players.append(tuple((p, team)))

    first_part = set()
    second_part = set()
    for player, team in players:
        age = relativedelta.relativedelta(date, player.birth_date)
        if (27 < age.years) and (age.years < 32):
            first_part.add(tuple((player, team)))
        elif (31 < age.years) and (age.years < 36):
            second_part.add(tuple((player, team)))
        elif age.years == 36:
            team.remove_player(player)
            contract_manager.remove_contract_player(player, date)
            player = generate_player(date, countries, team, player.get_post(), 17, 21, 19, 0.85)
            team.add_player(player)
            contract_manager.add_contract(player.get_id(), team.get_id_club(), date)

    for player, team in choices_bibi(list(first_part), k=round(len(first_part)*0.15)):
        team.remove_player(player)
        contract_manager.remove_contract_player(player, date)
        new_player = generate_player(date, countries, team, player.get_post(), 17, 21, 19, 0.85)
        team.add_player(new_player)
        contract_manager.add_contract(new_player.get_id(), team.get_id_club(), date)

    for player, team in choices_bibi(list(second_part), k=round(len(second_part)*0.85)):
        team.remove_player(player)
        contract_manager.remove_contract_player(player, date)
        new_player = generate_player(date, countries, team, player.get_post(), 17, 21, 19, 0.85)
        team.add_player(new_player)
        contract_manager.add_contract(new_player.get_id(), team.get_id_club(), date)