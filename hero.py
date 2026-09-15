import random
from fractions import Fraction

class Hero:
    def __init__(self, name):
        """instantiates a new hero"""
        self.name = name
        self.health = 125
        self.attack_power = 15

        self.mana_power = 10
        self.mana_max = 10
        self.fireball_attack = 10
        self.attack_list = [self.attack, self.slam, self.fireball]
        

    def attack(self):
        """return damage from hero"""
        print(f"{self.name} uses attack!")
        return random.randint(1, self.attack_power)

    def slam(self):
        print(f"{self.name} uses slam!")
        """less probable attack, returns damage (float)"""
        if random.randint(1,3) == 1:
            return self.attack() * 4
        return 0

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        global health
        return self.health > 0

    def fireball(self):
        """Magic attack, uses mana, returns damage"""
        print(f"{self.name} uses fireball!")
        if self.mana_power >= 4:
            self.mana_power -= 4
            return self.fireball_attack
        print("But it failed!")
        return 0

    
    def random_attack(self):
        return self.attack_list[random.randint(1, len(self.attack_list)-1)]()


