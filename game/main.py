import inquirer
import random

# creates 'Player' class which handles all important information about the player
class Player:
    def __init__(self, name, health, mana, strength, defence, damage, level, ch_class, inventory):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.damage = damage
        self.level = level
        self.ch_class = ch_class
        self.inventory = inventory

# creates an function asking for name on the beginning of each session
def ask_name():
    while True:
        creation = [
            inquirer.Text('name',
                        message='What\'s your name adventurer?',
                        ),
        ]
        name = inquirer.prompt(creation)
        if len(name['name']) == 0:
            continue
        elif len(name['name']) > 0:
            return name
        else: # if user is dumb enough to imput something not expected print this >-<
            print('There was an error with validating inputed information.')

# creates an function asking for class on the beginning of each session
def choose_class():
    options = [
        'Barbarian',
        'Ranger',
        'Wizard',
        'Necromancer'
    ]

    stats = {
        'Barbarian': {'health': 120, 'mana': 30, 'strength': 15, 'defence': 10, 'damage': 20},
        'Ranger': {'health': 100, 'mana': 70, 'strength': 10, 'defence': 8, 'damage': 20},
        'Wizard': {'health': 80, 'mana': 100, 'strength': 5, 'defence': 10, 'damage': 25},
        'Necromancer': {'health': 90, 'mana': 90, 'strength': 10, 'defence': 8, 'damage': 15},
    }

    questions = [
    inquirer.List('chosen_class',
                  message='What class would you like to choose?',
                  choices=options,
                  carousel=True
                  ),
    ]
    chosen_class = inquirer.prompt(questions)['chosen_class']

    if chosen_class in stats:
        return stats[chosen_class], chosen_class
    else:
        print('There was an error with validating chosen class.')
        return None, None

# assigns 'name' that has been imputed by the player to variable called name
name = ask_name()['name']
chosen_stats, chosen_class = choose_class()

if chosen_stats is not None:
    # assigns all base stats to player based on the chosen class
    player = Player(name, chosen_stats['health'], chosen_stats['mana'], chosen_stats['strength'], chosen_stats['defence'], chosen_stats['damage'], 1, chosen_class, [])
    print(f"Name: {player.name}")
    print(f"Health: {player.health}")
    print(f"Mana: {player.mana}")
    print(f"Strength: {player.strength}")
    print(f"Defence: {player.defence}")
    print(f"Damage: {player.damage}")
    print(f"Level: {player.level}")
    print(f"Class: {player.ch_class}")
    print(f"Inventory: {player.inventory}")

print(f"Welcome, {player.name}! You'll be playing as {chosen_class}")
