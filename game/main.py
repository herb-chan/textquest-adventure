import inquirer
import random

# define Character class
class Character:
    def __init__(self, name, health, mana, strength, defence, damage, level, character_class, inventory):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.defence = defence
        self.damage = damage
        self.level = level
        self.character_class = character_class
        self.inventory = inventory

# function which asks for the Player's name
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

# function which lets the user choose a character class and return the corresponding stats
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

# function which creates new character using the user's imput for name and class
def create_character():
    name = ask_name()['name']
    character_stats, character_class = choose_class()
    character = Character(
        name=name,
        health=character_stats['health'],
        mana=character_stats['mana'],
        strength=character_stats['strength'],
        defence=character_stats['defence'],
        damage=character_stats['damage'],
        level=1,
        character_class=character_class,
        inventory=[])
    return character

# main function which runs the character creation process
def main():
    character = create_character()
    print(f"Welcome, {character.name} the {character.character_class}!")

# run the main function when the script is executed
if __name__ == "__main__":
    main()