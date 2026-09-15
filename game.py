from goblin import Goblin
from hero import Hero
import copy


ARENA_NAME = "The Bowl"
ENEMIES_DEFEATED = 0

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

        hero.mana_power = min(10, hero.mana_power + 1)
        enemy.is_blocking = False

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")



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

    battle(john, goblin)

if __name__ == "__main__":
    main()
