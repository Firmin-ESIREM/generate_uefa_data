import json
from contract import Contract


class ContractManager:

    def __init__(self, file=None):
        self.contracts = dict()
        self.contracts_active = dict()
        self.file = file

    def add_contract(self, id_player, id_club, date):
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


    def extract_data(self, file):
        header = "date_debut_contrat;date_fin_contrat;club_contrat;joueur_contrat\n"
        for contract in self.contracts:
            header += self.contracts[contract].line()
        file.write(header)
        file.close()