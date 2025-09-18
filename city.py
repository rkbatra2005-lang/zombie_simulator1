import random
from characters import Human, Zombie

class City:
    def __init__(self, humans, zombies):
        self.humans = humans
        self.zombies = zombies
        self.turn = 1

    def run_simulation(self):
        print("\n===== Zombie Apocalypse Simulator =====\n")
        while self.humans and self.zombies:
            print(f"\n----- Turn {self.turn} -----")

            attacker = random.choice(self.humans + self.zombies)

            if isinstance(attacker, Human) and self.zombies:
                target = random.choice(self.zombies)
                attacker.attack(target)
                if not target.is_alive():
                    print(f"{target.__class__.__name__} destroyed!")
                    self.zombies.remove(target)

            elif isinstance(attacker, Zombie) and self.humans:
                target = random.choice(self.humans)
                attacker.attack(target)
                if not target.is_alive():
                    print(f"{target.__class__.__name__} is infected and turns into a Zombie!")
                    self.humans.remove(target)
                    self.zombies.append(Zombie())

            self.turn += 1

        if not self.humans:
            print("\n💀 All humans infected → Zombies win!")
        else:
            print("\n🔥 All zombies destroyed → Humans win!")

        print(f"\nGame ended in {self.turn-1} turns.")