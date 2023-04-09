import inquirer
from prettytable import PrettyTable
from tqdm import tqdm
from colored import fg, bg, attr
import time
import random

# COLOURS
red = fg('#ff5e57')
red2 = fg('#ff3f34')
green = fg('#0be881')
yellow = fg('#ffdd59')
blue = fg('#4bcffa')
res = attr('reset')

# STORY HERE PROBABLY BECAUSE IDK
def story_int():
    print(f'''
[{yellow} Story {res}]
    You are a young adventurer, eager to explore the world and seek your fortune. 
    You have heard tales of a great evil that threatens the land.
    You arrive in the small village of Millfield, where the people are suffering 
    from a mysterious malady that has drained the life from their crops and animals. 
    The villagers are desperate for help, and they turn to you for aid.
    ''')
    time.sleep(15)
    print(f'''
[{green} Millfield {res}]
    Nestled amidst rolling hills and sprawling fields, Millfield village stands as a testament to rustic charm. 
    The village center bustles with activity, as farmers and traders gather to sell their wares and share their stories. 
    But beyond the village lies a world of wonder, full of natural beauty and breathtaking vistas. 
    Lush forests and sun-kissed fields stretch as far as the eye can see, offering endless opportunities 
    for exploration and adventure. And with the rolling hills in the distance and the endless skies overhead, 
    the hero's journey is sure to be a memorable one, full of excitement, danger, and discovery.
''')
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
        else:  # if user is dumb enough to imput something not expected print this >-<
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

    def show_level():
        length = 100
        level_bar = tqdm(range(length), desc=f'Class level {character.level}', position=0)

    def show_stats():
        statistics = PrettyTable()
        statistics.field_names = [f'{red}❤ Health{res}', f'{blue}✎ Mana{res}',
                                  f'{red2}! Strength{res}', f'{green}❋ Defence{res}', f'{yellow}⚠ Damage{res}']
        statistics.add_row([character.health, character.mana,
                           character.strength, character.defence, character.damage])

        print(f'[{red}!{res}] You\'re playing as {character.character_class}! Below you can see all your statistics and class level!')
        print(statistics)
        show_level()

    def activities():
        options = [
            'Open your inventory',
            'Check your statistics',
            'Check your quests',
            'Check your bestiary'
        ]

        questions = [
            inquirer.List('activity',
                          message='What would you like to do?',
                          choices=options,
                          carousel=True
                          ),
        ]
        activity = inquirer.prompt(questions)['activity']

        if activity == 'Check your statistics':
            show_stats()

    story_int()

# run the main function when the script is executed
if __name__ == "__main__":
    main()
