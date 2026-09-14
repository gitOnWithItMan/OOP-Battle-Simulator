from goblin import Goblin
from hero import Hero
import copy


ARENA_NAME = "The Bowl"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Aiden Salsman")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    newGoblin = Goblin("Joshua Dobbins")
    print(f"{newGoblin.name} enters the arena with {newGoblin.health} health.")

    john = Hero("John")
    print(f"{john.name} enters the arena with {john.health} health.")

    attackDamage = john.attack()
    goblin.take_damage(attackDamage)
    print(f"Goblin now has {goblin.health}hp")
    if goblin.health > 0:
        john.take_damage(goblin.attack())
        print(f"John now has {john.health}hp")

if __name__ == "__main__":
    main()
