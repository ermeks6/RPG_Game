class Character:
    def __init__(self, name, health, mana, attack, defense):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack = attack
        self.defense = defense


class Player(Character):
    pass


class Enemy(Character):
    pass


def main():
    player = Player(name='Player', health=100, mana=50, attack=20, defense=10)
    enemy = Enemy(name='Enemy', health=80, mana=30, attack=15, defense=5)

    while player.health > 0 and enemy.health > 0:
        print('What would you like to do?')
        print('1. Attack')
        print('2. Cast spell')
        print('3. Wait')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            enemy.health -= player.attack
            print(f"{player.name} attacks {enemy.name} for {player.attack} damage!")
            print(f"{enemy.name}'s health is now {enemy.health}.")

        elif choice == 2:
            if player.mana >= 10:
                player.mana -= 10
                enemy.health -= player.attack * 2
                print(f"{player.name} casts a spell for {player.attack * 2} damage!")
                print(f"{enemy.name}'s health is now {enemy.health}.")
                print(f"{player.name}'s mana is now {player.mana}.")
            else:
                print(f"{player.name} doesn't have enough mana to cast a spell.")

        elif choice == 3:
            print(f"{player.name} waits.")

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

        if enemy.health > 0:
            player.health -= enemy.attack
            print(f"{enemy.name} attacks {player.name} for {enemy.attack} damage!")
            print(f"{player.name}'s health is now {player.health}.")

    if player.health <= 0:
        print(f"{player.name} has been defeated.")
    else:
        print(f"{enemy.name} has been defeated.")

if __name__ == '__main__':
    main()
