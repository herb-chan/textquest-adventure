import inquirer
import random

# creates 'Player' class which handles all important information about the player
class Player:
    def __init__(self, name, health, mana, strength, defence, damage, level, ch_class):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.damage = damage
        self.level = level
        self.ch_class = ch_class

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

# assigns 'name' that has been imputed by the player to variable called name
name = ask_name()['name']
# assigns all base stats to player
player = Player(name, 100, 50, 10, 5, 15, 1, 1)

print(f"Welcome, {player.name}!")

def chest_open():
    random_number = random.randInt(0,9)