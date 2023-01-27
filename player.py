from random import randint, choice
from os import listdir
from uuid import uuid4

first_names: dict[str, list[str]] = {}
last_names: dict[str, list[str]] = {}

for file in listdir("prenoms"):
    with open("prenoms/" + file, 'r', encoding="utf-8") as f:
        content = f.read().split("\n")
    first_names[file] = content

# print(first_names)

for file in listdir("noms"):
    with open("noms/" + file, 'r', encoding="utf-8") as f:
        content = f.read().split("\n")
    last_names[file] = content


class Player:
    def __init__(self, team, nationality, birth_date, post):
        self.id = str(uuid4())
        self.nationality = nationality
        self.birth_date = birth_date  # 17 à 35 ans
        self.current_club = team.id_team
        self.post = post
        self.first_name = ""
        self.last_name = ""

        if self.nationality == team.championship.country.id_nationality and randint(1, 20) <= 17:
            self.first_name = choice(first_names[self.nationality])
            self.last_name = choice(last_names[self.nationality])
        else:
            nn = list(first_names.keys())
            nn.remove(team.championship.country.id_nationality)
            nn = choice(nn)
            self.first_name = choice(first_names[nn])
            self.last_name = choice(last_names[nn])

    def get_post(self):
        return self.post

    def get_id(self):
        return self.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.first_name + ' ' + self.last_name.upper() + ' ' + str(self.birth_date) + ' ' + self.post
