import inquirer

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
            break
        else:
            print('There was an error with validating inputed information.')