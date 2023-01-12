import Joueur

class Team:

    def __init__(self,id: int,  name: str, id_championship: int):
        self.name = name
        self.id = id
        self.id_championship = id_championship
        self.players = []
        self.players_per_post = {"A": [], "M": [], "D": [], "G": []}

    def add_player(player: Joueur):
        if player not in self.players:
            self.players.append(player)
            self.players_per_post[player.get_post()].append(player)
    
    def remove_player(player: Joueur):
        if player not in self.players:
            self.players.remove(player)
            self.players_per_post[player.get_post()].remove(player)


    def get_players():
        return self.players

    def get_players_per_post(post):
        if post in self.players_per_post:
            return self.players_per_post[post]