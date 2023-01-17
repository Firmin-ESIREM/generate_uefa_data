from contract import Contract


class ContractManager:

    def __init__(self):
        self.contracts = dict()
        self.contracts_active = dict()

    def add_contract(self, id_player, id_club, date):
        contract = Contract(date, id_club, id_player)
        contract_id = contract.get_id()
        if id_player not in self.contracts_active:
            self.contracts[contract_id] = contract
            self.contracts_active[id_player] = contract
        else:
            contract_active = self.contract_active[id_player]
            self.remove_contract(contract_active.get_id(), date)
            self.contracts[contract_id] = contract
            self.contract_active[id_player] = contract

    def remove_contract(self, contract_id, date):
        player_id = self.contracts[contract_id].get_player_id()
        self.contracts[contract_id].close(date)
        self.contracts_active.pop(player_id)
