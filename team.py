from championship import Championship
from player import Player


class Team:
    def __init__(self, id_team: str, id_championship: str, championships: list[Championship], id_commune) -> None:
        self.id_team: str = id_team
        self.championship: Championship = next((x for x in championships if x.id_championship == id_championship), None)
        self.players: list[Player] = []
        self.players_per_post: dict[str, list[Player]] = {"A": [], "M": [], "D": [], "G": []}
        self.commune_id = id_commune
        
    def __eq__(self, other):
        return other.get_id_club() == self.id_team
    
    def get_commune_id(self):
        return self.commune_id

    def add_players(self, players: list[Player]):
        for player in players:
            self.add_player(player)

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

    def get_players_per_post(self, post: str):
        return self.players_per_post[post]

    def get_amount_players(self):
        return len(self.players)

    def get_id_club(self):
        return self.id_team

    def get_id_championship(self):
        return self.championship.get_id()