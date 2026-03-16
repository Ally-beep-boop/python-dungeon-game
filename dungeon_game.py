import random
import time

# Create a class called 'Monster' that takes a name, hit points value,
# and attack value
class Monster:

    def __init__(self, name, hit_points, attack_value):
        self.name = name
        self.hit_points = hit_points
        self.max_hit_points = hit_points
        self.attack_value = attack_value
    
    # Methods to take damage and determine whether they are alive
    def take_damage(self, amount):
        self.hit_points -= amount
        if self.hit_points < 0:
            self.hit_points = 0
    
    def is_alive(self):
        return self.hit_points > 0

# Create a class called 'Player'
class Player:

    def __init__(self, name):
        self.name = name
        self.hit_points = 100
        self.max_hit_points = 100
        self.attack_value = 15

    # Similar methods to take damage and determine whether they are alive
    # Add extra method to print player stats
    def take_damage(self, amount):
        self.hit_points -= amount
        if self.hit_points < 0:
            self.hit_points = 0
    
    def is_alive(self):
        return self.hit_points > 0
    
    def show_stats(self):
        print(f"Hello {self.name}! Your current hits are {self.hit_points},"
              f"and your maximum hits are {self.max_hit_points}")

# Create a function called get_random_monster()
# and create a list of three monsters
def get_random_monsters():
    monsters = [
        {"name": "Goblin", "hp": 30, "attack": 20},
        {"name": "Skeleton", "hp": 20, "attack": 10},
        {"name": "Troll", "hp": 80, "attack": 50}
    ]
    m = random.choice(monsters)
    return Monster(m["name"], m["hp"], m["attack"])

# Create a second function with get_boss() that returns a single tough Monster
def get_boss():
    return Monster("Dragon", 200, 75)

# Write a function called comabt(player, monster) that takes both objects and
# runs a fight between them
def combat(player, monster):
    print(f"\nA wild {monster.name} appears!")

    # Create a while loop that continues as long as both the player and monster
    # are alive
    while player.is_alive() and monster.is_alive():

        # Ask user if they want to attack or run
        action = input("\nDo you want to attack or run? (attack/run): ")

        # If they choose to attack, calculate a random damage amount, apply it
        # to the monster, then let the monster hit back if it's still alive
        if action.lower() == "attack":
            damage = random.randint(0, player.attack_value)
            monster.take_damage(damage)
            print(f"\nYou attack the {monster.name} for {damage} damage!")

            if monster.is_alive():
                monster_damage = random.randint(0, monster.attack_value)
                player.take_damage(monster_damage)
                print(f"\nThe {monster.name} attacks you back for "
                      f"{monster_damage} damage!")
                
        # If the player chooses to run, print a message
        elif action.lower() == "run":
            print(f"\nYou run away from the {monster.name}!")
            return "fled"
        
        # If they enter an invalid action, print a message and continue the loop
        else:
            print("\nInvalid action. Please choose 'attack' or 'run'.")
            continue

        # Print players current hit points
        print(f"\nYour current hit points: {player.hit_points}")

    # If player defeats the monster, print a message and return won
    if player.is_alive():
        print(f"\nYou defeated the {monster.name}!")
        return "won"
    
    # If the monster defeats the player, print a message and return lost
    else:
        return "lost"

# Write a function called play() that asks the user for their name, create a
# Player object
def play():
    user_name = input("\nEnter your name: ")
    player = Player(user_name)

    # Use a for loop to run through three rounds of combat with a random monster
    # and call combat() each time
    for _ in range(3):
        monster = get_random_monsters()
        combat(player, monster)

        # If the player dies, end the game and print a message
        if not player.is_alive():
            print("\nYou have been defeated! Game over.")
            return
        
        # If the player survives, give them a small hp heal before the next room
        player.hit_points = min(player.hit_points + 20, player.max_hit_points)
        print("\nYou take a moment to rest and heal some hit points.")
        time.sleep(2)

    # If the player survives all three rounds, have them fight the boss
    if player.is_alive():
        print("\nYou have survived the three rounds of combat! Now it's time to "
              "face the boss!")
        boss = get_boss()
        combat(player, boss)

        if player.is_alive():
            print("\nCongratulations! You have defeated the boss and won the game!")
        else:
            print("\nYou have been defeated by the boss! Game over.")

# Call the play() function to start the game
if __name__ == "__main__":
    play()