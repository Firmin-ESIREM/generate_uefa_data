import json
from contract import Contract


class ContractManager:

    def __init__(self):
        self.contracts = dict()
        self.contracts_active = dict()

    def add_contract(self, id_player, id_club, date):
        """with open("contracts.json", "w") as f:
            b = dict()
            for key, value in self.contracts.items():
                value_str = str(value.id)
                value_date_start = str(value.date_start)
                value_date_end = str(value.date_end)
                value_id_player = str(value.id_player)
                value_id_club = str(value.id_club)
                b[str(key)] = {"id": value_str, "date_start": value_date_start, "date_end": value_date_end,
                               "id_player": value_id_player, "id_club": value_id_club}
            f.write(json.dumps(b))
        with open("active_contracts.json", "w") as f:
            a = dict()
            for key, value in self.contracts_active.items():
                value_str = str(value.id)
                value_date_start = str(value.date_start)
                value_date_end = str(value.date_end)
                value_id_player = str(value.id_player)
                value_id_club = str(value.id_club)
                a[str(key)] = {"id" : value_str, "date_start": value_date_start, "date_end": value_date_end, "id_player": value_id_player, "id_club": value_id_club}
            f.write(json.dumps(a))"""
        contract = Contract(date, id_club, id_player)
        contract_id = contract.get_id()
        if id_player not in self.contracts_active:
            self.contracts[contract_id] = contract
            self.contracts_active[id_player] = contract
        else:
            contract_active = self.contracts_active[id_player]
            self.remove_contract(contract_active.get_id(), date)
            self.contracts[contract_id] = contract
            self.contracts_active[id_player] = contract

    def get_contract_id(self, player):
        for contract in self.contracts_active:
            if player.get_id() == contract:
                return self.contracts_active[contract]

    def __str__(self):
        return str(self.contracts_active)

    def remove_contract(self, contract_id, date):
        player_id = self.contracts[contract_id].get_player_id()
        self.contracts[contract_id].close(date)
        self.contracts_active.pop(player_id)

    def remove_contract_player(self, player, date):
        contract_id = self.contracts_active[player.get_id()].get_id()
        self.contracts[contract_id].close(date)
        self.contracts_active.pop(player.get_id())
