import random

class Hero:
    def __init__(self, name):
        """instantiates a new hero"""
        self.name = name
        self.health = 125
        self.attack_power = 15

    def attack(self):
        """return damage from hero"""
        return random.randint(1, self.attack_power)

    def slam(self):
        """less probable attack, returns damage (float)"""
        if random.randint(1,3) == 1:
            return self.attack_power * 2.5
        return 0

    def take_damage(self, damage):
        damaged = self.health - damage
        if damaged > 0:
            self.health = damaged

    def is_alive(self):
        return self.health > 0

