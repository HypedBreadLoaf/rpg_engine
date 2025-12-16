import classes, random, items_spells
from classes import print_b
main_inv = {}
player1 = classes.BlackMage(name='Lucas', hp=100, mp=100, weapon='Adaga de lobo', armor='Couraça de ferro', lv=2, exp=0, inv=main_inv, spells=[items_spells.spells['Ultimato']])
player2 = classes.Knight(name='Maria', hp=100, mp=100, weapon='Adaga de lobo', armor='Couraça de ferro', lv=2, exp=0, inv=main_inv)
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
        else:
            for enemy in monsters:
                if enemy.die == False:
                        enemy.attack(party, monsters)
            for member in party:
                mp = 10
                print_b(f'{member.name} ganhou {mp} de MP.')
                member.mp += 10
    print_b('--------------------------------------')

def spawn(value, quantity):
    monsters = []
    if quantity == 2:
        if value == 1:
            for id in range(2):
                monsters.append(classes.MinorWolf(id))
        elif value == 2:
            monsters.append(classes.AlphaWolf(0))
            monsters.append(classes.MinorWolf(1))
        return monsters
    elif quantity == 3:
        if value == 1:
            for id in range(3):
                monsters.append(classes.MinorWolf(id))
        elif value == 2:
            monsters.append(classes.AlphaWolf(0))
            for id in range(2):
                monsters.append(random.choices([classes.MinorWolf(id+1), classes.AlphaWolf(id+1)], [70, 30])[0])
        return monsters
     
while True:
    for member in current_party:
        lvs.append(member.lv)
    lv_average = sum(lvs)/len(lvs)
    if lv_average >= 1 and lv_average < 2:
        spawn_value = 1
    elif lv_average >= 2 and lv_average < 3:
        spawn_value = 2
    battle(current_party, spawn(spawn_value, random.choice([2,3])))