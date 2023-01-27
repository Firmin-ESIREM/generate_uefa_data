from random import choice, choices
from datetime import datetime
from dateutil import relativedelta


def mercato(championship_list, players_number: int, teams_per_championship, date: datetime, contract_manager,
            teams_per_id):
    """
    This function simulates a transfer market.
    """
    retirement(championship_list, teams_per_championship, date, contract_manager, teams_per_id)
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


def retirement(championships, teams_per_championship, date, contract_manager, teams_per_id):
    players = list()
    for championship in championships:
        teams = teams_per_championship[championship.get_id()]
        for team1 in teams:
            team = teams_per_id[int(team1)]
            for p in team.get_players():
                print("b")
                print(p)
                players.append(tuple((p, team)))
    first_part = list()
    second_part = list()
    for player, team in players:
        age = relativedelta.relativedelta(date, player.birth_date)
        if 28 <= age.years <= 31:
            first_part.append(tuple((player, team)))
        elif 32 <= age.years <= 35:
            second_part.append(tuple((player, team)))
        elif age.years == 36:
            team.remove_player(player)
            contract_manager.remove_contract(player, date)
            # TODO générer un nouveau pélo
    for player, team in choices(first_part, round(len(first_part)*0, 15)):
        team.remove_player(player)
        contract_manager.remove_contract(player, date)
        # TODO générer un nouveau pélo
    for player, team in choices(second_part, round(len(second_part)*0, 85)):
        team.remove_player(player)
        contract_manager.remove_contract(player, date)
        # TODO générer un nouveau pélo