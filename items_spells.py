class Weapon():
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

class Armor():
    def __init__(self, name, resistance):
        self.name = name
        self.resistance = resistance

weapons = {
    'Adaga de lobo': Weapon('Adaga de lobo', 100)}
armors = {
    'Couraça de ferro': Armor('Couraça de ferro', 0.95)}