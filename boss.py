from enemy import Enemy
import random


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health=250, attack_power=30)

    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")

        multiplier = 1
        if random.randint(1,5) == 1:
            print("A CRITICAL HIT!")
            multiplier = 2

        return multiplier * (damage + bonus_damage)