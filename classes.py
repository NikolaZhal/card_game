class Card:
    def __init__(self, attack, cost):
        self.attack = attack
        self.cost = cost

    def make_hod(self):
        ...
    
    def get_info(self):
        return {'attack': self.attack, 'cost': self.cost}