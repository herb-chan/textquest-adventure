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
        self.inventory = inventory or []

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
        'Bard',
        'Cleric',
        'Druid',
        'Fighter',
        'Monk',
        'Paladin',
        'Ranger',
        'Rogue',
        'Sorcerer',
        'Warlock',
        'Wizard'
    ]

    questions = [
    inquirer.List('chosen_class',
                  message='What class would you like to choose?',
                  choices=options,
                  carousel=True
                  ),
    ]
    answers = inquirer.prompt(questions)

# assigns 'name' that has been imputed by the player to variable called name
name = ask_name()['name']
# assigns all base stats to player
player = Player(name, 100, 50, 10, 5, 15, 1, 1)

print(f"Welcome, {player.name}!")

def chest_open():
    random_number = random.randInt(0,9)