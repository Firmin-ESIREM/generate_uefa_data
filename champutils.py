class ChampUtils:

    def __init__(self):
        self.points = dict()

    def add_point(self, id_champ, id_club, points):
        if id_champ not in self.points:
            self.points[id_champ] = {id_club: points}
        else:
            if id_club not in self.points[id_champ]:
                self.points[id_champ][id_club] = points
            else:
                self.points[id_champ][id_club] += points

    def close(self):
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
        self.reset()
        return results

    def reset(self):
        self.points = dict()
