import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.is_blocking = False
        self.attack_list = [self.attack, self.focus, self.block]

    def attack(self):
        """Return a random amount of damage."""
        print(f"{self.name} is attacking!")
        return random.randint(1, self.attack_power)

    def focus(self):
        """Increases goblin damage, returns zero"""
        print(f"{self.name} is focusing!")
        self.attack_power += 5
        return 0
    

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        if self.is_blocking:
            damage /= 4
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0

    def block(self):
        """Cannot take damage this round, returns 0"""
        print(f"{self.name} is blocking!")
        self.is_blocking = True
        return 0

    def random_attack(self):
        return self.attack_list[random.randint(1, len(self.attack_list)-1)]()