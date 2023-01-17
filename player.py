from random import choice
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

print(first_names)
print(last_names)


class Player:
    def __init__(self, id_club, nationality, birth_date, post):
        self.nationality = nationality
        self.birth_date = birth_date  # 17 à 35 ans
        self.current_club = id_club
        self.post = post


        self.first_name
        self.last_name

    def get_post(self):
        return self.post
