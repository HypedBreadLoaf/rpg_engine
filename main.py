import classes, random
from classes import print_b
main_inv = {}
player1 = classes.BlackMage('Lucas', 100, 'Adaga de lobo', 'bbbb', 1, 0, main_inv)
#player1.use_spell()
#print(player1.name)
player2 = classes.Knight('Maria', 100, 'Adaga de lobo', 'aaaa', 1, 0, main_inv)
#wolf = classes.MinorWolf()
players = [player1, player2]
#wolf.attack(players)
#print(player1.hp)
#print(player2.hp)
#player1.action(player1.name, player1.role)
#player2.action(player2.name, player2.role)

lv_average = 0
lvs = []
current_party = [player1, player2]

def battle(party, monsters):
    if len(monsters) == 2:
        print_b(f'A party foi atacada por {monsters[0].name} e {monsters[1].name}!')
    elif len(monsters) == 3:
        print_b(f'A party foi atacada por {monsters[0].name}, {monsters[1].name} e {monsters[2].name}!')
    while True:
        for member in party:
            member.action(member.name, member.role, monsters)
            for enemy in monsters:
                enemy.check_die()
        for enemy in monsters:
            enemy.attack(party)


def spawn(value, quantity):
    monsters = []
    if quantity == 2:
        if value == 1:
            for id in range(2):
                monsters.append(classes.MinorWolf(id))
        return monsters
    elif quantity == 3:
        if value == 1:
            for id in range(3):
                monsters.append(classes.MinorWolf(id))
        return monsters
     
while True:
    for member in current_party:
        lvs.append(member.lv)
    lv_average = sum(lvs)/len(lvs)
    if lv_average >= 1 and lv_average <= 2:
        spawn_value = 1
    battle(current_party, spawn(spawn_value, random.choice([2,3])))