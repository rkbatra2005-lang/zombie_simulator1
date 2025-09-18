from .character import Character

class Zombie(Character):
    def __init__(self, health=80, infection_power=10):
        super().__init__(health)
        self._infection_power = infection_power

    def attack(self, human):
        print(f"Zombie bites {human.__class__.__name__}! → {self._infection_power} damage.")
        human.take_damage(self._infection_power)


class StrongZombie(Zombie):
    def __init__(self, health=120, infection_power=15):
        super().__init__(health, infection_power)

    def attack(self, human):
        damage = self._infection_power + 10
        print(f"StrongZombie smashes {human.__class__.__name__}! → {damage} damage.")
        human.take_damage(damage)


class FastZombie(Zombie):
    def __init__(self, health=60, infection_power=8):
        super().__init__(health, infection_power)

    def attack(self, human):
        print(f"FastZombie swiftly bites {human.__class__.__name__}! → {self._infection_power} damage.")
        human.take_damage(self._infection_power)