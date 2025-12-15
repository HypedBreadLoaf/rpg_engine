import classes, random
from classes import print_b
main_inv = {}
player1 = classes.BlackMage('Lucas', 100, 'Adaga de lobo', 'Couraça de ferro', 1, 0, main_inv)
player2 = classes.Knight('Maria', 100, 'Adaga de lobo', 'Couraça de ferro', 1, 0, main_inv)
players = [player1, player2]
lv_average = 0
lvs = []
current_party = [player1, player2]

def battle(party, monsters):
    if len(monsters) == 2:
        print_b(f'A party foi atacada por {monsters[0].name} e {monsters[1].name}!')
    elif len(monsters) == 3:
        print_b(f'A party foi atacada por {monsters[0].name}, {monsters[1].name} e {monsters[2].name}!')
    all_dead = len(monsters)
    while True:
        for member in party:
            current_dead = 0
            member.action(monsters)
            for enemy in monsters:
                if enemy.die == False:
                    enemy.check_die(party)
            for enemy in monsters:
                if enemy.die == True:
                    current_dead += 1
            if current_dead == all_dead:
                print_b('A party venceu!')
                break
        if current_dead == all_dead:
            break
        for enemy in monsters:
            if enemy.die == False:
                    enemy.attack(party)
    print_b('--------------------------------------')

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