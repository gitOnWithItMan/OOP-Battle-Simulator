import random


class Goblin:
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 15
        self.is_blocking = False

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)

    def focus(self):
        """Increases goblin damage, returns nothing"""
        self.attack_power += 5
        print(f"{self.name} is focusing!")

    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        """Return True while the goblin has health remaining."""
        return self.health > 0

    def block(self):
        """Cannot take damage this round, returns nothing"""
        self.is_blocking = True