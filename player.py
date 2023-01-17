from random import randint, choice
from os import listdir


first_names: dict[str, list[str]] = {}
last_names: dict[str, list[str]] = {}

for file in listdir("prenoms"):
    with open("prenoms/" + file, 'r') as f:
        content = f.read().split("\n")
    first_names[file] = content

for file in listdir("noms"):
    with open("noms/" + file, 'r') as f:
        content = f.read().split("\n")
    last_names[file] = content


class Player:
    def __init__(self, team, nationality, birth_date, post):
        self.nationality = nationality
        self.birth_date = birth_date  # 17 à 35 ans
        self.current_club = team.id_team
        self.post = post
        self.first_name: str
        self.last_name: str

        if self.nationality == team.championship.country.id_nationality:
            if randint(1, 20) > 17:
                nn = list(first_names.keys())
                nn.remove(self.nationality)
                nn = choice(nn)
                print(nn)
                self.first_name = choice(first_names[nn])
                self.last_name = choice(last_names[nn])
            else:
                self.first_name = choice(first_names[self.nationality])
                self.last_name = choice(last_names[self.nationality])

    def get_post(self):
        return self.post

    def __str__(self):
        return "" # self.first_name + ' ' + self.last_name.upper()
