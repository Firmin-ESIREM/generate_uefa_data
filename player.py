from random import choice


class Joueur:
    def __init__(self, id_club, nationality, first_names, last_names):
        self.nationality = nationality
        self.first_name = choice(first_names)
        self.last_name = choice(last_names)
        self.birth_date  # 17 à 35 ans
        self.current_club = id_club
        self.post

    def get_post(self):
        return self.post
