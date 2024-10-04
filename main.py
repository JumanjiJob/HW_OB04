from abc import ABC, abstractmethod

class Weapon(ABC):
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print('Боец выбирает меч')
        print('Боец наносит удар мечом')

class Bow(Weapon):
    def attack(self):
        print('Боец выбирает лук')
        print('Боец стреляет из лука')

class Fighter():

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        self.weapon.attack()

class Monster():
    pass

fighter = Fighter()

fighter.change_weapon(Sword())
fighter.change_weapon(Bow())