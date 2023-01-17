class Match:

    def __init__(self, championship_id, date: datetime, id_club1, id_club2, commune_match):
        self.date = date
        self.id_club1 = id_club1
        self.id_club2 = id_club2
        self.commune_match = commune_match


    def simulate(self, champ_utils):
        winner = random.choice([id_club1, id_club2, None])
        if winner is None:
            self.winner = "N"
            self.points_domicile = 1
            self.points_exterieur = 1
            champ_utils.add_point(self.championship_id, self.id_club1, 1)
            champ_utils.add_point(self.championship_id, self.id_club2, 1)
        elif winner.get_commune_id() == self.commune_match:
            champ_utils.add_point(self.championship_id, winner, 3)
            self.points_domicile = 3
            self.points_exterieur = 0
            self.winner = "D"
        else:
            if self.id_club1 != winner:
                winner = self.id_club1 
            else:
                winner = self.id_club2
            champ_utils.add_point(self.championship_id, winner, 3)
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
