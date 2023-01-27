class ChampUtils:

    def __init__(self):
        self.points = dict()
        self.file_vainqueur = open("data-test/vainqueur.csv", "w", encoding="utf-8")
        self.file_points = open("data-test/points.csv","w", encoding="utf-8")
        self.file_vainqueur.write("annee_vainqueur;championnat_vainqueur;club_vainqueur;points_vainqueur\n")
        self.file_points.write("annee_points;championnat_points;nombre_points;club_points\n")

    def add_point(self, id_champ, id_club, points):
        if id_champ not in self.points:
            self.points[id_champ] = {id_club: points}
        else:
            if id_club not in self.points[id_champ]:
                self.points[id_champ][id_club] = points
            else:
                self.points[id_champ][id_club] += points

    def close(self, date):
        results = dict()
        for championship in self.points:
            best_points = -1
            best_club = None
            for club in self.points[championship]:
                points = self.points[championship][club]
                if points > best_points:
                    best_points = points
                    best_club = club
            results[championship] = (best_club, best_points)
        self.file_points.write(self.points_line(date))
        self.file_vainqueur.write(self.vainqueur_line(date, results))
        self.reset()
        return results
    def reset(self):
        self.points = dict()

    def vainqueur_line(self, date, results):
        final_string = ""
        for championship in results:
            id_club, points = results[championship]
            final_string += f"{date.year};{championship};{id_club};{points}\n"
        return final_string
    def points_line(self, date):
        final_string = ""
        for championship in self.points:
            for club in self.points[championship]:
                points = self.points[championship][club]
                final_string += f"{date.year};{championship};{points};{club}\n"
        return final_string

    def __str__(self):
        string = "{"
        for championnat in self.points:
            string += f"{championnat}" + " : {"
            for club in self.points[championnat]:
                string += f"{club}" + ": " + f"{self.points[championnat][club]}" + ", "
            string += "}, "
        string += "}"
        return string

    def end(self):
        self.file_vainqueur.close()
        self.file_points.close()