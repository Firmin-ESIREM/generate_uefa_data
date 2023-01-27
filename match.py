from datetime import datetime
import random


class Match:

    def __init__(self, championship_id, date: datetime, club1, club2, commune_match):
        self.date = date
        self.club1 = club1
        self.club2 = club2
        self.championship_id = championship_id
        self.commune_match = commune_match
        self.w = None
        self.l = None

    def simulate(self, champ_utils):
        winner = random.choice([self.club1, self.club2, None])
        if winner is None:
            self.winner = "N"
            self.w = self.club1
            self.l = self.club2
            self.points_domicile = 1
            self.points_exterieur = 1
            champ_utils.add_point(self.championship_id, int(self.club1.get_id_club()), 1)
            champ_utils.add_point(self.championship_id, int(self.club2.get_id_club()), 1)
        elif winner.get_commune_id() == self.commune_match:
            champ_utils.add_point(self.championship_id, int(winner.get_id_club()), 3)
            self.points_domicile = 3
            self.points_exterieur = 0
            self.w = winner
            self.l = self.club2 if winner == self.club1 else self.club1
            self.winner = "D"
        else:
            if self.club1 != winner:
                winner = self.club1
                self.w = self.club1 
                self.l = self.club2
            else:
                winner = self.club2
                self.w = self.club2
                self.l = self.club1
            champ_utils.add_point(self.championship_id, int(winner.get_id_club()), 3)
            self.points_domicile = 0
            self.points_exterieur = 3
            self.winner = "E"
        
        if self.winner == "N":
            nb_buts = random.randint(0, 3)
            self.score_domicile = nb_buts
            self.score_exterieur = nb_buts
        elif self.winner == "E":
            nb_buts_win = random.randint(1,4)
            nb_buts_los = random.randint(0,nb_buts_win-1)
            self.score_exterieur = nb_buts_win
            self.score_domicile = nb_buts_los
        else: 
            nb_buts_win = random.randint(1,4)
            nb_buts_los = random.randint(0,nb_buts_win-1)
            self.score_exterieur = nb_buts_los
            self.score_domicile = nb_buts_win

        self.tirs_cadres_domicile = random.randint(1, 15)
        self.tirs_cadres_exterieur = random.randint(1, 15)
        self.tirs_non_cadres_domicile = random.randint(2, 30)
        self.tirs_non_cadres_exterieur = random.randint(2, 30)

    def to_csv(self):
        return f"{self.championship_id};{self.date.year}-{self.date.month}-{self.date.day};club1;club2;{self.score_domicile};{self.score_exterieur}"

    def __str__(self):
        return f"w: {self.w.get_id_club()} l : {self.l.get_id_club()} winner : {self.winner} but_ext : {self.score_exterieur} but_int : {self.score_domicile} points_int : {self.points_domicile} points_ext : {self.points_exterieur} tirs_cadres_ext : {self.tirs_cadres_exterieur} tirs_cadres_int : {self.tirs_cadres_domicile} tirs_non_cadres_ext : {self.tirs_non_cadres_exterieur} tir_non_cadres_inte : {self.tirs_non_cadres_domicile}"