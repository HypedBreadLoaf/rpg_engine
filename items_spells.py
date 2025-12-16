class Weapon():
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

class Armor():
    def __init__(self, name, resistance):
        self.name = name
        self.resistance = resistance

class Spell():
    def __init__(self, name, num, mp_cost, spell_type, targets):
        self.name = name
        self.num = num
        self.type = spell_type
        self.mp_cost = mp_cost
        self.targets = targets

weapons = {
    'Adaga de lobo': Weapon('Adaga de lobo', 50)}

armors = {
    'Couraça de ferro': Armor('Couraça de ferro', 0.95)}

spells = {
    'Ultimato': Spell('Ultimato', 125, 100, 'O', 'all')
}