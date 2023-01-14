from championship import Championship
from player import Player


class Team:
    def __init__(self, id_team: str, id_championship: str, championships: list[Championship]) -> None:
        print(championships)
        self.id_team: str = id_team
        self.championship: Championship = next((x for x in championships if x.id_championship == id_championship), None)
        self.players = []
        self.players_per_post = {"A": [], "M": [], "D": [], "G": []}

    def add_player(self, player: Player):
        if player not in self.players:
            self.players.append(player)
            self.players_per_post[player.get_post()].append(player)

    def remove_player(self, player: Player):
        if player not in self.players:
            self.players.remove(player)
            self.players_per_post[player.get_post()].remove(player)

    def get_players(self):
        return self.players
