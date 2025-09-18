from .character import Character

class Human(Character):
    def __init__(self, health=100, weapon="pistol"):
        super().__init__(health)
        self._weapon = weapon

    def attack(self, zombie):
        damage = 20
        print(f"Human attacks Zombie with {self._weapon}! → {damage} damage.")
        zombie.take_damage(damage)


class Soldier(Human):
    def __init__(self, health=120, weapon="rifle"):
        super().__init__(health, weapon)

    def attack(self, zombie):
        damage = 40
        print(f"Soldier fires {self._weapon} at Zombie! → {damage} damage.")
        zombie.take_damage(damage)


class Medic(Human):
    def __init__(self, health=90, weapon="healing kit"):
        super().__init__(health, weapon)

    def attack(self, zombie):
       print(f"Medic heals a human instead of attacking.")