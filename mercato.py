from random import choice, choices


def mercato(championship_list, players_number: int, teams_per_championship):
    """
    This function simulates a mercato.
    """
    numbers_players_to_draft = round(players_number * 0.035)  # Get the approximate number of players to need drafts
    for x in range(numbers_players_to_draft):
        championships = choices(championship_list, k=2)  # I get two randoms championships
        teams = list()  # I create a list for add two randoms teams
        for championship in championships:
            id_champ = championship.get_id()  # I get the id of the championship
            teams.append(teams_per_championship[id_champ][choice(
                teams_per_championship[id_champ])])  # I add a random team in this championship
        player1 = choice(teams[0].get_players())  # I choose a random player in this team
        player2 = choice(
            teams[1].get_players_per_post(player1.get_post()))  # I choose a player with the SAME post in the other team
        teams[0].remove(player1)  # I switch players into teams
        teams[1].remove(player2)
        teams[1].add(player1)
        teams[0].add(player2)
        # TODO contracts
