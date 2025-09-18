from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health):
        self._health = health  # Encapsulation

    @property
    def health(self):
        return self._health

    def take_damage(self, damage):
        self._health -= damage
        print(f"{self.__class__.__name__} takes {damage} damage → Health: {self._health}")

    @abstractmethod
    def attack(self, target):
        pass

    def is_alive(self):
        return self._health > 0