from characters import Human, Soldier, Medic, Zombie, StrongZombie, FastZombie
from city import City

def start_game():
    humans = [
        Human(100, "knife"),
        Soldier(120, "rifle"),
        Medic(90, "healing kit")
    ]

    zombies = [
        Zombie(80, 10),
        StrongZombie(120, 15),
        FastZombie(60, 8)
    ]

    city = City(humans, zombies)
    city.run_simulation()


if __name__ == "__main__":
    while True:
        start_game()
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("\nThanks for playing the Zombie Apocalypse Simulator!")
            break