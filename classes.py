import items_spells, random, time, sys

def print_b(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print('', end='\n')

def text_action(name, rpg_class):
    print_b(f'O que {name} vai fazer?')
    print_b(f'Atacar (A)')
    print_b(f'Usar item (I)')
    print_b(f'Se defender (D)')
    if rpg_class == 'Black Mage':
        print_b(f'Usar magia ofensiva (M)')
    elif rpg_class == 'Knight':
        print_b(f'Atrair ataque inimigo (S)')

class Party_Member():
    def __init__(self, name, hp, weapon, armor, lv, exp, inv):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.armor = armor
        self.lv = lv
        self.exp = exp
        self.inv = inv

    def check_lvl_up(self):
        if self.lv == 1 and self.exp >= 100:
            self.lv += 1
            self.exp -= 100
            print_b(f'{self.name} subiu de nível! {self.lv-1} -> {self.lv}')
        elif self.lv == 2 and self.exp >= 250:
            self.lv += 1
            self.exp -= 250
            print_b(f'{self.name} subiu de nível! {self.lv-1} -> {self.lv}')
        elif self.lv == 3 and self.exp >= 500:
            self.lv += 1
            self.exp -= 500
            print_b(f'{self.name} subiu de nível! {self.lv-1} -> {self.lv}')
    
    def attack(self, enemies):
        while True:
            try:
                print_b(f'Quem {self.name} irá atacar?')
                for enemy in enemies:
                    if enemy.die == False:
                        print_b(enemy.name + ' ' + "("+(str(enemy.id+1))+")")
                action_command = int(input()) - 1
                if enemies[action_command].die == True:
                    print_b('Esse inimigo já foi derrotado!')
                    continue
                dmg = int(items_spells.weapons[self.weapon].dmg + items_spells.weapons[self.weapon].dmg * (self.lv - 1) * 0.05)
                enemies[action_command].hp -= dmg
                print_b(f'{enemies[action_command].name} levou {dmg} de dano!')
                break
            except ValueError:
                print_b('Você digitou errado!')
            
        

    def use_item(self):
        pass

    def defend(self):
        pass

    def action(self, enemies):
        options = ['A', 'I', 'D']
        while True:
            print_b(f'O que {self.name} ({self.role}) vai fazer?')
            print_b(f'Atacar (A)')
            print_b(f'Usar item (I)')
            print_b(f'Se defender (D)')
            if self.role == 'Black Mage':
                print_b(f'Usar magia ofensiva (M)')
                options.append('M')
            elif self.role == 'Knight':
                print_b(f'Atrair ataque inimigo (S)')
                options.append('S')

            action_command = input('->').upper()
            if action_command == 'A':
                self.attack(enemies)
            elif action_command == 'I':
                self.use_item()
            elif action_command == 'D':
                self.defend()
            elif self.role == 'Black Mage' and action_command == 'M':
                self.use_spell()
            elif self.role == 'Knight' and action_command == 'S':
                self.rally()
            else: 
                print_b('Você digitou algo diferente.')
                continue
            break

class BlackMage(Party_Member):
    def __init__(self, name, hp, weapon, armor, lv, exp, inv):
        super().__init__(name, hp, weapon, armor, lv, exp, inv)
        self.role = 'Black Mage'

    def use_spell(self):
        print_b('Spell was used')
    

class Knight(Party_Member):
    def __init__(self, name, hp, weapon, armor, lv, exp, inv):
        super().__init__(name, hp, weapon, armor, lv, exp, inv)
        self.role = 'Knight'
    
    def rally(self):
        print_b('Rallied')

class Monster():
    def __init__(self, id, name, hp, drops, exp_drop):
        self.id = id
        self.name = name
        self.hp = hp
        self.drops = drops
        self.exp_drop = exp_drop
        self.die = False
        
    def attack(self):
        pass
    #Ver se consegue colocar o metodo de ataque aqui, alem de checar se está vivo para atacar

    def check_die(self, party):
        if self.hp <= 0:
            self.die = True
            print_b(f'{self.name} foi derrotado! A party ganhou {self.exp_drop} de experiência.')
            for member in party:
                member.exp += self.exp_drop
                member.check_lvl_up()

    
class MinorWolf(Monster):
    def __init__(self, id):
        super().__init__(id, name = 'Lobo menor', hp = 100, drops = [items_spells.weapons['Adaga de lobo']], exp_drop = 20)

    def mordida(self, target):
        dano = round(15 * items_spells.armors[target.armor].resistance)
        print_b(f'Lobo menor usou "Mordida" em {target.name} e deu {dano} de dano!')
        target.hp -= dano

    def investida(self, target):
        dano = round(10 * items_spells.armors[target.armor].resistance)
        print_b(f'Lobo menor usou "Investida" em {target.name} e deu {dano} de dano!')
        target.hp -= dano

    def attack(self, players):
        target = random.choice(players)
        random.choices([self.mordida, self.investida], [40, 60])[0](target) #Vai retonar [self.metodo]. Por isso o [0], para então ficar self.metodo(target)