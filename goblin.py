import random

from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        super().__init__(name)
        self.is_blocking = False
        self.attack_list = [self.attack, self.focus, self.block]

    def focus(self):
        """Increases goblin damage, returns zero"""
        print(f"{self.name} is focusing!")
        self.attack_power += 5
        return 0

    def block(self):
        """Cannot take damage this round, returns 0"""
        print(f"{self.name} is blocking!")
        self.is_blocking = True
        return 0

    def random_attack(self):
        return self.attack_list[random.randint(1, len(self.attack_list)-1)]()