from datetime import datetime
from uuid import uuid4


class Contract:

    def __init__(self, date_start: datetime, id_club: int, id_player: int):
        self.id = str(uuid4())
        self.date_start = date_start
        self.date_end = None
        self.id_player = id_player
        self.id_club = id_club

    def __str__(self):
        return f"[Contract] id : {str(self.id)} | date_start : {str(self.date_start)} | date_end : {str(self.date_end)} | id_player : {str(self.id_player)} | id_club : {str(self.id_club)}"
    def get_id(self):
        return self.id

    def get_player_id(self):
        return self.id_player

    def is_active(self):
        return self.date_end is None

    def close(self, date: datetime):
        self.date_end = date
