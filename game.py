import itertools
import random
import sys
import time


# Board
def MIN_WIDTH() -> int:
    """Represent the minimum width of the board.

    :postcondition: returns an integer that represents the minimum width of the board
    :return: an integer 0 representing the minimum width of the board
    """
    return 0


def MAX_WIDTH() -> int:
    """Represent the maximum width of the board.

    :postcondition: returns an integer that represents the maximum width of the board
    :return: an integer 25 representing the maximum width of the board
    """
    return 25


def MIN_HEIGHT() -> int:
    """Represent the minimum height of the board.

    :postcondition: returns an integer that represents the minimum height of the board
    :return: an integer 0 representing the minimum height of the board
    """
    return 0


def MAX_HEIGHT() -> int:
    """Represent the maximum height of the board.

    :postcondition: returns an integer that represents the maximum width of the board
    :return: an integer 25 representing the maximum height of the board
    """
    return 25


# Pokemon Classes
def GRASS() -> dict:
    """Represent the Grass class attributes.

    :postcondition: returns a dictionary that represent that stats that the Grass class possesses
    :return: a dictionary containing default information about the class of Grass
    """
    class_dict = dict(class_name="Grass",
                      level_one_name="Bulbasaur", level_two_name="Ivysaur", level_three_name="Venusaur",
                      hp=40, max_hp=40, hp_growth=20,
                      exp_required_to_level=200,
                      min_damage=10, max_damage=16,
                      damage_growth=5,
                      special_attack="Solar Beam",
                      special_attack_multiplier=1.5)
    return class_dict


def WATER() -> dict:
    """Represent the Grass class attributes.

    :postcondition: returns a dictionary that represent that stats that the Water class possesses
    :return: a dictionary containing default information about the class of Water
    """
    class_dict = dict(class_name="Water",
                      level_one_name="Squirtle", level_two_name="Warturtle", level_three_name="Blastoise",
                      hp=30, max_hp=30, hp_growth=15,
                      exp_required_to_level=250,
                      min_damage=15, max_damage=21,
                      damage_growth=5,
                      special_attack="Hydropump",
                      special_attack_multiplier=2)
    return class_dict


def FIRE() -> dict:
    """Represent the Grass class attributes.

    :postcondition: returns a dictionary that represent that stats that the Fire class possesses
    :return: a dictionary containing default information about the class of Fire
    """
    class_dict = dict(class_name="Fire",
                      level_one_name="Charmander", level_two_name="Charmelion", level_three_name="Charizard",
                      hp=20, max_hp=20, hp_growth=10,
                      exp_required_to_level=300,
                      min_damage=15, max_damage=26,
                      damage_growth=15,
                      special_attack="Flamethrower",
                      special_attack_multiplier=2.5)
    return class_dict


def ELECTRIC() -> dict:
    """Represent the Grass class attributes.

    :postcondition: returns a dictionary that represent that stats that the Electric class possesses
    :return: a dictionary containing default information about the class of Electronic
    """
    class_dict = dict(class_name="Electric",
                      level_one_name="Pichu", level_two_name="Pikachu", level_three_name="Raichu",
                      hp=15, max_hp=15, hp_growth=10,
                      exp_required_to_level=350,
                      min_damage=20, max_damage=31,
                      damage_growth=20,
                      special_attack="Thunder Bolt",
                      special_attack_multiplier=3)
    return class_dict


# Level up
def EXP_GAINED_PER_KILL() -> int:
    """Return the amount of experience gained per foe killed.

    :postcondition: returns an integer representation of the experience gained per foe killed
    :return: an integer 150 representing the gained EXP per kill
    """
    return 150


# Combat
def FOE_NAMES() -> tuple:
    """Return the list of possible foe names.

    :postcondition: returns a list of possible foe names
    :return: a list of strings containing names of foe
    """
    names = ("Weevil", "El Nino", "Blast Fungus", "Walder", "Parasite", "Sparrow")
    return names


def FOE_APPEAR_CHANCE() -> int:
    """Return an integer that represents the chance of foe appearing.

    :postcondition: returns a integer that represents the 20 percent of chance that the user
    encounters a foe when moving
    :return: an integer 20 representing the chance of being back stabbed by foe when fleeing
    """
    return 20


def BACK_STAB_CHANCE() -> int:
    """Return an integer that represents the chance of being back stabbed when attempting to run away.

    :postcondition: returns a integer that represents the 20 percent of chance
    of being back stabbed when attempting to run away
    :return: an integer 20 representing the chance of being back stabbed by foe when fleeing
    """
    return 20


def HEALING_RATE() -> int:
    """Return an integer that represents healing rate.

    :postcondition: returns a integer that represents the healing rate
    :return: an integer 4 representing the healing rate
    """
    return 4


def RUN_AWAY() -> int:
    """Represent that represents the the character has run away from a battle as the constant integer.

    :postcondition: always returns 7(lucky seven)
    :return: a integer 77 that represents the character has run away from a battle
    """
    return 77


def DRAW_GAME() -> int:
    """Represent that the character died as the constant integer.

    :postcondition: returns 0
    :return: a integer 0 that represents the draw game
    """
    return 0


def CHARACTER_DEAD() -> int:
    """Represent that the character died as the constant integer.

    :postcondition: returns 1
    :return: a integer that represents the character died
    """
    return 1


def FOE_DEAD() -> int:
    """Represent that a foe died as the constant integer.
    :postcondition: Always return 2
    :return: A integer that represents a foe died
    """
    return 2


# Movement system
def create_board() -> list:
    """Make a board represented by a list of 625 tuples.

    :postcondition: make a board list containing 625 tuples of location
    :return: a list containing 625 tuples in 25X25 matrix
    """
    # Make the board with list comprehension
    board = [(row, column) for row in range(MAX_WIDTH()) for column in range(MAX_HEIGHT())]
    return board


def print_board(character: dict):
    """Visualize the board and the current location of the character.

    :param character: a dictionary containing character's information
    precondition: character must contain valid character information key value pairs
    :precondition: location must be a list containing 2 integers
    """
    location = (character["location"][0], character["location"][1])
    print(f"* Current location: ({character['location'][0]}, {character['location'][1]}) *")
    for column in range(MAX_HEIGHT()):
        for row in range(MAX_WIDTH()):
            if row == location[0] and column == location[1]:
                print("🧔 ", end="")
            elif row == 5 and column == 5:
                print("👿 ", end="")
            elif row == location[0] and column == location[1] - 1:
                print("1️⃣ ", end="")
            elif row == location[0] - 1 and column == location[1]:
                print("2️⃣ ", end="")
            elif row == location[0] and column == location[1] + 1:
                print("3️⃣ ", end="")
            elif row == location[0] + 1 and column == location[1]:
                print("4️⃣ ", end="")
            else:
                print("🌱 ", end="")
        print("")


def check_move_in_board(board: list, location: tuple) -> bool:
    """Verify if the movement is valid.

    :param board: a list containing location information
    :param location: a tuple containing row and column
    :precondition: board is a list representing 5X5 tuple matrix
    :precondition: location is a tuple containing the next location of the character
    :postcondition: verifies if user's location is valid or not
    :return: True for valid movement or False when movement is out of baord
    >>> test_board =   [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), \
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), \
                    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), \
                    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), \
                    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    >>> test_location = (2,3)
    >>> check_move_in_board(test_board, test_location)
    True
    >>> test_location = (6,5)
    >>> check_move_in_board(test_board, test_location)
    False
    """
    return location in board


def get_character_location(character: dict) -> list:
    """Get the character's location.

    :param character: a dictionary that contains character status
    precondition: character must be a valid character and hp must greater than 0
    :postcondition: return the valid character location
    :return: a list contains the character coordinates
    >>> character_dict = {"location":[0, 0]}
    >>> get_character_location(character_dict)
    [0, 0]
    >>> character_dict = {"location":[5, 5]}
    >>> get_character_location(character_dict)
    [5, 5]
    """
    return character["location"]


def move(character: dict, direction: str, board: list) -> bool:
    """Move character's location if movement is valid.

    :param character: a dictionary containing character_status
    :param direction: a string represent the direction
    :param board: a list that has 25 locations(5X5 matrix)
    :precondition: character must contain correct character status key value pairs
    :precondition: The direction must be '1' to North, '2' to West, '3' to South or '4' to East
    :precondition: The board must be a list of 25 tuples representing coordinate locations
    :postcondition: moves character location if valid
    :return: a boolean
    >>> test_board = create_board()
    >>> character_dict = {'name':'Lily', 'hp': 10, 'location':[4, 3]}
    >>> move(character_dict, '2', test_board)
    True
    >>> character_dict = {'name':'Lily', 'hp': 10, 'location':[24, 24]}
    >>> move(character_dict, '3', test_board)
    False
    """
    location = get_character_location(character)
    if direction == "1" and character["location"][1] != MIN_HEIGHT():
        location[1] -= 1  # move to the north
    elif direction == "2" and character["location"][0] != MIN_WIDTH():
        location[0] -= 1  # move to the west
    elif direction == "3" and character["location"][1] != MAX_HEIGHT() - 1:
        location[1] += 1  # move to the south
    elif direction == "4" and character["location"][0] != MAX_WIDTH() - 1:
        location[0] += 1  # move to the east
    else:
        return False

    if check_move_in_board(board, tuple(location)):
        character["location"] = location
        return True

    return False


# Make the character
def create_character() -> dict:
    """Ask the user to make the character name and assign initial status of character.

    :postcondition: assigns a dictionary containing the initial status of character
    :return: a dictionary containing initial status of character
    """
    # Ask user for the character name
    character_name = input("\033[1;33m**What's your name? ** \033[0m")
    user_class_input = get_class_from_user()
    chosen_class = class_selector(user_class_input)
    character = dict(name=character_name,
                     location=[0, 0],
                     level=1,
                     exp=0)
    character = character | chosen_class  # Combine character chosen_class dictionary

    print(f"You chose the {character['class_name']} class. Your pokemon is {character['level_one_name']}.")
    command_message(character)
    return character


def get_class_from_user() -> str:
    """Return a correct user chosen class number.

    :precondition: input must be a valid string
    :postcondition: user will be asked for the valid input
    :postcondition: returns a correct user chosen class number
    :return: a string
    """
    options = ["1", "2", "3", "4"]
    acceptable_input = False
    while not acceptable_input:
        user_input = input("What class do you want to play as? \n1. Grass\n2. Water\n3. Fire\n4. Electric\n").strip()
        if user_input in options:
            return user_input
        else:
            print("Invalid input. Try again.")


def class_selector(chosen_class: str) -> dict:
    """Return a class dictionary.

    :param chosen_class: a string
    :precondition: chosen_class must be a string that is either '1', '2', '3', or '4'
    :postcondition: returns a class dictionary
    :return: a dictionary

    >>> test_input = '1'
    >>> class_selector(test_input) #doctest: +NORMALIZE_WHITESPACE
    {'class_name': 'Grass', 'level_one_name': 'Bulbasaur', 'level_two_name': 'Ivysaur', 'level_three_name': 'Venusaur',
    'hp': 40, 'max_hp': 40, 'hp_growth': 20, 'exp_required_to_level': 200, 'min_damage': 10, 'max_damage': 16,
    'damage_growth': 5, 'special_attack': 'Solar Beam', 'special_attack_multiplier': 1.5}

    >>> test_input = '4'
    >>> class_selector(test_input) #doctest: +NORMALIZE_WHITESPACE
    {'class_name': 'Electric', 'level_one_name': 'Pichu', 'level_two_name': 'Pikachu', 'level_three_name':
    'Raichu', 'hp': 15, 'max_hp': 15, 'hp_growth': 10, 'exp_required_to_level': 350, 'min_damage': 20,
    'max_damage': 31, 'damage_growth': 20, 'special_attack': 'Thunder Bolt', 'special_attack_multiplier': 3}
    """

    if chosen_class == "1":  # enter "1" to play as the Grass class
        return GRASS()
    elif chosen_class == "2":  # enter "2" to play as the Water class
        return WATER()
    elif chosen_class == "3":  # enter "3" to play as the Fire class
        return FIRE()
    elif chosen_class == "4":  # enter "4" to play as the Electric class
        return ELECTRIC()


def heal(character: dict):
    """Add HP to the character's current health points.

    :param character: a dictionary
    :precondition: character must be a dictionary containing character status key value pairs
    :precondition: character's HP does not exceed max_hp
    :postcondition: increase the character's HP but not past their max_hp

    >>> character_status = {'hp':31, 'max_hp': 40}
    >>> heal(character_status)
    >>> character_status["hp"]
    35
    >>> heal(character_status)
    >>> character_status["hp"]
    39
    >>> heal(character_status)
    >>> character_status["hp"]
    40
    """
    # Heal hp if you do not have full hp already
    character["hp"] = min(character["hp"] + HEALING_RATE(), character["max_hp"])


def damage_character(character: dict, damage_scale: int) -> bool:
    """Decrease the character health point and check if the character is dead.

    :param character: a dictionary containing character status
    :param damage_scale: the amount of health points to decrease
    :precondition: character must contain correct character status
    :precondition: damage_scale must be a positive integer
    :postcondition: update decreased character health point in the dictionary of charater
    :return: True(character died) or False(character alive)
    >>> character_status = {'hp':10,'location': [2, 4]}
    >>> damage_character(character_status, 12)
    True
    >>> character_status = {'hp':10,'location': [2, 4]}
    >>> damage_character(character_status, 4)
    False
    """
    character["hp"] -= damage_scale  # update character's hp

    return character["hp"] <= 0  # If HP is less than or equal to 0, the character is dead


def damage_boss(boss: dict, damage_scale: int) -> bool:
    """Return True while updating the boss's decreased HP or return False when if boss's HP is less than 0.

    :param boss: a dictionary containing the boss status
    :param damage_scale: the damage_scale of HP by the character
    :precondition: boss is a dictionary containing the foe status
    :precondition: damage_scale is an integer representing the damage_scale of HP
    :postcondition: return True or False representing the status of boss's HP
    :return: Ture for the foe's still alive or False for the foe is dead
    """
    boss["hp"] -= damage_scale  # update boss' hp

    return boss["hp"] <= 0  # If HP is less than or equal to 0, the boss is dead


def get_user_input(request: str) -> str:
    """Get the command based on user's request.

    :param request: a string, user's input on the command line
    :precondition: request(user input) must be a string among "quit", "list", and "foe"
    :precondition: if user's input is not one of "quit", "list" and "foe", return to
    default command
    :postcondition: return the command as user's request
    :return: none if the user typed "quit", or else return what the user asks
    """
    command = input(request).lower().strip()  # Ask for command from the user, user input must be a string

    if "quit" == command:  # If user inputs "quit"
        sys.exit()  # The program ends
    elif "list" == command:  # If user inputs "list"
        show_movement_options()  # Show the commands for each direction
    elif "foe" == command:  # If user inputs "foe"
        show_foes()  # Show the list of foes
    else:
        return command  # Otherwise, ask the user for input again


# Foe
def foe_appear() -> bool:
    """Generate random number to determine if a foe appears or not.

    :precondition: the possibility a foe appears is 20 percents.
    :postcondition: return True if random number is equal or greater than 20,
    else return False
    :return: True to determine a foe appears, False to determine a foe doesn't appear
    """
    roll_chance = random.randint(1, 100)  # generate the number that determines a foe appears or not in range 1 to 100
    if roll_chance <= FOE_APPEAR_CHANCE():  # there is 20 percent of chance a foe appears
        return True
    else:
        return False


def create_foe(character: dict) -> dict:
    """Return a foe based on the character's level if a foe appears.

    :param character: a dictionary containing the character's information
    :precondition character: must be a dictionary containing a key value pair representing character level
    :precondition: the power of foes is determined depends on character's level
    :postcondition: returns a created foe's dictionary if one appears based on the character's level
    :return: a dictionary of foe information
    """
    if foe_appear():  # The case a foe doesn't appear
        # make the easiest foe for level one character
        if character["level"] == 1:
            foe_name = dict((foe_order, foe) for foe_order, foe in enumerate(FOE_NAMES()))
            foe = dict(name=foe_name[random.randint(0, len(foe_name) - 1)], hp=10, min_damage=1, max_damage=10)

        # make the intermediate foe for level two character
        elif character["level"] == 2:
            foe_name = dict((foe_order, foe) for foe_order, foe in enumerate(FOE_NAMES()))
            foe = dict(name=foe_name[random.randint(0, len(foe_name) - 1)], hp=15, min_damage=5, max_damage=15)

        # make the hardest foe for level three character
        else:
            foe_name = dict((foe_order, foe) for foe_order, foe in enumerate(FOE_NAMES()))
            foe = dict(name=foe_name[random.randint(0, len(foe_name) - 1)], hp=20, min_damage=10, max_damage=20)

        return foe


def damage_foe(foe: dict, damage_scale: int) -> bool:
    """Return True while updating the foe's decreased HP or return False when if foe's HP is less than 0.

    :param foe: a dictionary containing the foe status
    :param damage_scale: the damage_scale of HP by the character
    :precondition: foe_status must be a dictionary containing the correct foe status
    :precondition: character must contain correct character status
    :precondition: damage_scale is an integer representing the damage_scale of HP
    :postcondition: return True or False representing the status of foe's HP
    :return: Ture for the foe's still alive or False for the foe is dead
    >>> foe_dict = {'hp': 10}
    >>> test_damage_scale = 2
    >>> damage_foe(foe_dict, test_damage_scale)
    False
    >>> foe_dict = {'hp': 10}
    >>> test_damage_scale = 4
    >>> damage_foe(foe_dict, test_damage_scale)
    False
    """
    foe["hp"] -= damage_scale  # Update decreased foe's HP
    return foe["hp"] <= 0  # If HP is equal or less than 0, the foe is dead


# Combat system
def roll_die():
    """Generate a random integer to determine who will be the first striker.

    :precondition: a random integer is in the range 1 to 20
    :postcondition: gets a random integer
    :return: a random integer to determine the first striker
    """
    return random.randint(1, 100)


def attack_boss(character_speed: int, boss_speed: int, character: dict, boss: dict):
    """Fight and return the combat result.

    :param character_speed: a positive integer in the dictionary of character,
    representing the result of roll_die()
    :param boss_speed: a positive integer in the dictionary of character,
    representing the result of roll_die()
    :param character: the dictionary containing character information
    :param boss: the dictionary containing boss information
    :precondition: character_speed and boss_speed must a positive integer
    :precondition: if character_speed is bigger than boss_speed, character attacks fist otherwise the boss attacks first
    :precondition: if boss_speed is bigger than character_speed, boss attacks fist otherwise the boss attacks first
    :precondition: 1 means the character died, False means the boss died
    :precondition: character must be a dictionary containing character status
    :precondition: boss must be a dictionary containing boss status
    :postcondition: returns the combat result represented by an integer 1 or False
    :return: an integer 1 or False which represents the combat result
    """
    # determine boss's damage strength
    boss_damage = random.randint(boss["min_damage"], boss["max_damage"])
    # determine character's damage strength
    character_damage = random.randint(character["min_damage"], character["max_damage"])

    if boss_speed > character_speed:  # boss strikes first
        combat_boss_message(boss_damage)  # display the damage dealt to the character
        if damage_character(character, boss_damage):  # If the character is defeated
            game_over_message()
            return CHARACTER_DEAD()

    elif character_speed > boss_speed:  # character strikes first
        print(f"You attacked the Boss. The boss lost {character_damage} HP.")
        # hp of boss is equal or less than 0
        if damage_boss(boss, character_damage):
            you_win_message()  # display victory text
            return is_boss_alive(boss), False  # When the boss has been defeated


def combat_round_with_boss(character: dict, boss: dict) -> int:
    """Fight with the boss until one of them dies.

    :param character: a dictionary containing character status
    :param boss: a dictionary containing foe status
    :precondition: the combat will be fight to death
    :precondition: character must be a valid dictionary and hp must be greater than 0
    :precondition: boss must contain a dictionary of boss status and hp must be greater than 0
    :postcondition: returns 1 or 2 representing the battle result
    :return: a integer 1 or 2 representing either character win or boss win
    """
    while character["hp"] > 0 and boss["hp"] > 0:
        character_speed = roll_die()  # assign the character's speed
        boss_speed = roll_die()  # assign the boss's speed

        # start attack, the first striker depends on the speed
        attack_boss(character_speed, boss_speed, character, boss)
        time.sleep(1.5)

    # character is defeated
    if character["hp"] <= 0:
        return CHARACTER_DEAD()

    # boss is defeated
    elif boss["hp"] <= 0:
        return FOE_DEAD()  # You finally beat the game!!!!


def attack(character_speed: int, foe_speed: int, character: dict, foe: dict) -> int:
    """Fight and return the combat result.

    :param character_speed: a positive integer in the dictionary of character,
    representing the result of roll_die()
    :param foe_speed: a positive integer in the dictionary of foe,
    representing the result of roll_die()
    :param character: the dictionary containing character status
    :param foe: the dictionary containing foe_status
    :precondition: character_speed and foe_speed must a positive integer
    :precondition: if character_speed is bigger than foe_speed, character attacks fist
    :precondition: if foe_speed is bigger than character_speed, foe attacks fist
    :precondition: return value 0 means a draw, 1 means the character died, 2 means the foe died
    :precondition: character must be a dictionary containing character status
    :precondition: foe must be a dictionary containing character status
    :postcondition: returns the combat result represented by an integer 0 or 1 or 2
    :return: an integer 0 or 1 or 2, which represents the combat result
    """
    foe_damage = random.randint(foe["min_damage"], foe["max_damage"])

    # Range of the attack strength of the character is determined by the level
    character_damage = random.randint(character["min_damage"], character["max_damage"])

    if character_speed < foe_speed:  # character strikes first
        combat_result_message(foe, foe_damage)
        if damage_character(character, foe_damage):  # if the character is defeated
            print(f"\033[1;31mYou were defeated by {foe['name']} \033[0m")
            game_over_message()
            return CHARACTER_DEAD()
    elif character_speed > foe_speed:  # foe strikes first
        print(f"You attacked {foe['name']}. The demon lost {character_damage} HP")
        if damage_foe(foe, character_damage):  # if the foe is defeated
            print(f"\033[1;35mThe {foe['name']} has been defeated\033[0m")
            return FOE_DEAD()  # foe is defeated

        return DRAW_GAME()  # the battle is not decided yet


def combat_round(character: dict, foe: dict, action: str) -> int:
    """Take an action 'kill' or 'runaway', and return the combat_result or runaway_result.

    :param character: a dictionary containing character status key value pairs
    :param foe: a dictionary containing foe status key value pairs
    :param action: a string represents the action based on user's request
    :precondition: character must contain a dictionary of character status
    :precondition: foe must contain a dictionary of foe status, and action must be a string
    :precondition: action must be a string
    :postcondition: attempt to run if user inputs command to run
    :postcondition: returns the battle result
    :return: an integer
    """
    combat_result = DRAW_GAME()

    if action == "k":  # user enters "k" to fight
        round_start(character, foe, action)  # begin combat
        return combat_result  # update combat result
    if not action == "k":  # user enters anything else to fight
        print("You attempt to run!")
        for _ in range(0, 4):
            print(".")
            time.sleep(0.3)

        if not back_stab(character, foe):  # if you run away safely
            print("You got away successfully!")


def round_start(character: dict, foe: dict, action: str):
    """Battle until either the character dies or flees, or the foe dies or flees.

    :param character: a dictionary containing character status
    :param foe: a dictionary containing foe status
    :param action: a string represents the action based on user's input
    :precondition: character must be a valid character dictionary
    :precondition: character must be a valid foe dictionary
    :precondition: if action is 'k', the user will enter the combat otherwise the user will try to flee
    :postcondition: simulates the speed of foe and character, the chance that a foe flees and starts the combat round
    """
    while character["hp"] > 0 and foe["hp"] > 0:
        character_speed = roll_die()  # assign the character's speed
        foe_speed = roll_die()  # assign the foe's speed
        if random.randint(1, 5) > 1:  # 20% chance of foe running away
            attack(character_speed, foe_speed, character, foe)  # attack if for doesn't run

            if foe["hp"] > 0 and character["hp"] > 0:  # both character and foe are alive
                display_character_info(character)  # display character status
                get_user_input("['k': keep fighting], [anything else: run away]")  # choose to continue fighting or run
            if not action:  # if the user doesn't input "k"
                break  # break out of the while loop
        else:  # if the foe flees
            foe_runs_away(character, foe)
            break  # get out of the while loop

    if character["hp"] > 0 >= foe["hp"]:  # character defeats foe and is alive
        win_battle(character, foe)


def win_battle(character: dict, foe: dict):
    """Shows the combat result when character wins and leve_up when reaching desired EXP.

    :param character:  a dictionary containing character status key value pairs
    :param foe: a dictionary containing foe status key value pairs
    :precondition: this function will only be called when the character won the battle
    :precondition: the character's hp must be greater than 0
    :postcondition: character will gain experience and level up if possible
    :postcondition: displays the battle result
    """
    if character["hp"] > 0 >= foe["hp"]:  # character defeats foe and is alive
        level_up(character)  # gain experience and possibly level up
        display_character_info(character)  # display character status


def back_stab(character: dict, foe: dict) -> bool:
    """Stab back by the foe when trying to flee.

    :param character: a dictionary containing character status
    :param foe: a dictionary containing foe status
    :precondition: the function will be called when the user tries to flee
    :precondition: there is 20% chance of runway failing
    :precondition: character must be valid and hp must be greater than 0
    :postcondition: updates character's decreased HP after being attacked back by the foe
    return: True or False
    """
    if random.randint(1, 100) <= BACK_STAB_CHANCE():  # 20% chance of getting back stabbed
        print(f"You attempt to run for it!! However, {foe['name']} stabbed you in the back!! ")
        damage_scale = random.randint(foe['min_damage'], foe['max_damage'])  # foe's damage
        damage_character(character, damage_scale)  # character takes damage from being back stabbed
        combat_result_message(foe, damage_scale)  # display damage stats
        if character["hp"] > 0:  # If character is still alive
            display_character_info(character)  # show character stats
        return True
    return False


def level_up(character: dict):
    """Level up if the user gains EXP required to level up.

    :param character: a dictionary containing character status key value pairs
    :precondition: character's health point must be greater than 0
    :postcondition: increase experience points of the character and check if the character has leveled up

    >>> character_dict = {'class_name':'Grass', 'exp': 250, 'level_one_name': 'Bulbasaur', 'level_two_name': 'Ivysaur',\
    'level_three_name': "Venusaur", 'hp':'40', 'max_hp':'40', 'hp_growth': '20', \
    'exp_required_level_two':200, 'exp_required_level_three': 300, 'min_damage':10, 'max_damage': 16, 'damage_growth':5}
    >>> test_character = dict(name='Victor', location=[1, 0], level=1, class_name='Grass', exp=0,\
                                level_one_name='Bulbasaur', level_two_name='Ivysaur', level_three_name="Venusaur",\
                                hp='40', max_hp='40', hp_growth='20', exp_required_to_level=200,\
                                min_damage=10, max_damage=16, damage_growth=5)
    >>> level_up(test_character)
    You gained [92m150[00m exp from this battle!
    """

    character["exp"] += EXP_GAINED_PER_KILL()  # gain experience after defeating a foe
    print(f"You gained \033[92m{EXP_GAINED_PER_KILL()}\033[00m exp from this battle!")

    if character["exp"] >= character["exp_required_to_level"]:  # level up!
        character["exp"] %= character["exp_required_to_level"]

        # update base stats
        character["min_damage"] += character["damage_growth"]
        character["max_damage"] += character["damage_growth"]
        character["max_hp"] += character["hp_growth"]
        character["level"] += 1

        display_level_up(character)


def foe_runs_away(character: dict, foe: dict):
    """Continue the game when foe flees.

    :param character: a dictionary containing character status key value pairs
    :param foe: a dictionary containing foe status key value pairs
    :precondition: this function will only be  called when foe is fleeing
    :precondition: there is 20% chance of that foe is fleeing at the end of the battle round
    :precondition: HP of the character must be larger than 0
    :postcondition: draw game when the foe is fleeing
    :postcondition: print messages to let user know the foe is fleeing
    """
    if character["hp"] > 0:
        DRAW_GAME()
        print(f"{foe['name']} ran away!!!")
        print(f"[Current Status: LEVEL \033[92m{character['level']}\033[00m, \033[92m{character['exp']}\033[00m EXP"
              f"\033[92m{character['hp']}\033[00m HP ]")


# Command Messages
def opening_message():
    """Print game opening text.
    :postcondition: prints the game opening text
    '"""

    for greeting in map(str.strip, str.upper("-------**Welcome to the Kanto region of the Pokemon Universe**--------")):
        print(greeting, end=' ')
    print("")
    print("You caught wind of Pokemon experimentation in Team Rockets secret lab.")
    print("You have successfully infiltrated Team Rocket's lab.")
    print("Your mission is to defeat Team Rocket and stop their operations.")
    print("You are not alone! You and your chosen Pokemon will fight against Team Rocket's experiments together.")
    print("Your Pokemon will evolve every time you level up, up to their final 3rd evolution.")
    print("There's no time to waste, you enter the lab.")


def command_message(character: dict):
    """Print command guide messages.

    :param character: a dictionary containing character key value pairs
    :precondition: character must contain a list containing character information
    :postcondition: print command messages
    """
    print(f"You enter Team Rocket's lab, {character['name']}.")
    print("There are chimera Pokemon lurking around every corner.")
    print("You can find the boss at (5,5)")
    print("Make sure you are strong enough to beat it!! Being at least Level 3 is recommended ")
    print("-----------------------------------MENU-----------------------------------------")
    print("<< Type the key below and press Enter >>")
    print("['1': North, '2': West, '3': South: '4': East]")
    print("['list': movement command list, 'foe': description of foes]")
    print("['quit': end the game]")
    print("--------------------------------------------------------------------------------")


def show_movement_options():
    """Print a list showing the user the movement options.
    :postcondition: prints a list showing the user the movement options
    """

    options = ["North", "West", "South", "East"]
    direction_list = [direction_numbers for direction_numbers in zip(itertools.count(1), options)]

    for index in range(len(direction_list)):
        print(f'Enter {direction_list[index][0]} brings you to {direction_list[index][1]}')


def show_foes():
    """Print information about the foes.
    :postcondition: print information about the foes
    """

    foe_names = FOE_NAMES()
    foe_description = ["This Pokemon is a grass-type Pokemon and slightly resembles a leopard. It has huge ears, "
                       "vine-like fur and a tail full of flowers.",
                       "This Pokemon is a fire-type Pokemon and slightly resembles a hedgehog. It has powerful legs, "
                       "huge ears and a black snout.",
                       "This Pokemon is a ice-type Pokemon and shares features with a termite. It has icy skin, a fur "
                       "covered mouth and muscular legs.",
                       "This Pokemon is a dark-type Pokemon and bears resemblance to an albatross. It has smoke-like "
                       "wings, a rugged beak and black and white feathers.",
                       "This Pokemon is a bug-type Pokemon and somewhat resembles an ant. It has a little mouth, thorny"
                       "skin and ridged legs."]
    foe_options = [foe_list for foe_list in zip(foe_names, foe_description)]
    for index in range(len(foe_options)):
        print(f"[{foe_options[index][0]}] : {foe_options[index][1]}")


def combat_result_message(foe: dict, damage_scale: int):
    """Tell the user about the combat_result.

    :param foe: a dictionary containing foe status
    :param damage_scale: a number showing how much the character was hurt
    :precondition: the foe_status must contain a dictionary containing foe status key value pairs
    :precondition damage_scale: must be a positive integer
    :postcondition: show the message telling the user's decreased HP and the name of foe
    :postcondition: prints a string message
    """
    print(f"The {foe['name']} attacked you. You lost {damage_scale} HP")


def display_level_up(character: dict):
    """Display character's level up information.

    :param character: a dictionary containing character_status
    :precondition: character must contains a dictionary containing character status key value pairs
    :precondition: this function will be called when character leveling up
    :precondition: character only can see this message two times when leveling up to 2 and 3
    :postcondition: shows character's updated level, new power, and evolved pokemon
    """
    print(f"You leveled up to level {character['level']}!"
          f"\nYou now deal from {character['min_damage']} to {character['max_damage'] - 1} damage!"
          f"\nYour max hp has increased by {character['hp_growth']} hp for a total of {character['max_hp']} hp.")
    if character["level"] == 1:
        print(f"Your current Pokemon evolution is {character['level_one_name']}.")
    elif character["level"] == 2:
        print(f"Your current Pokemon evolution is {character['level_two_name']}.")
    else:
        print(f"Your current Pokemon evolution is {character['level_three_name']}.")


def combat_boss_message(damage_scale: int):
    """Tell the user about the combat_result.

    :param damage_scale: a number showing how much the character was hurt
    :precondition: the foe must contain a list containing foe status key value pairs
    :precondition damage_scale: must be a positive integer
    :postcondition: show the message telling the user's decreased HP and the name of foe
    :postcondition: prints a string message
    """
    print(f"The Boss attacked you. You lost {damage_scale} HP")


def display_character_health(character: dict):
    """Print the character's current Health Points.

    :param character: a dictionary containing character_status
    :precondition: character must contains a dictionary containing character status key value pairs
    :postcondition: prints a string message representing character's HP
    :postcondition: prints a string message which shows combat_result
    """

    if character["level"] == 1:
        print(f"[Current HP: {character['hp']}, your Pokemon: {character['level_one_name']}]")
    elif character["level"] == 2:
        print(f"[Current HP: {character['hp']}, your Pokemon: {character['level_two_name']}]")
    else:
        print(f"[Current HP: {character['hp']}, your Pokemon: {character['level_three_name']}]")


def display_character_info(character: dict):
    """Print the character's information.

    :param character: a dictionary containing character_status
    :precondition: character must contain correct character status
    :postcondition: prints the information about character's current level, exp and HP
    """

    print(f"[Current Status: LEVEL \033[92m{character['level']}\033[00m, \033[92m{character['exp']}\033[00m EXP, "
          f"\033[92m{character['hp']}\033[00m HP ]")


def game_over_message():
    """Print the game_over message when character's hp is equal or smaller than 0.

    :precondition: this function will be called when the character is dead by a foe or the boss
    :postcondition: prints ASCII art on the screen about game over message
    """
    print("")
    print("""\033[1;31m
    #     #                  ######                  
     #   #   ####  #    #    #     # # ###### #####  
      # #   #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #####  #    # 
       #    #    # #    #    #     # # #      #    # 
       #    #    # #    #    #     # # #      #    # 
       #     ####   ####     ######  # ###### #####  
                                                  
                                                    
    \033[0m""")
    print("** You failed to save the Pokemon. They continue to be experimented on. **")


def you_win_message():
    """Print winning message when the character defeats the boss.

    :precondition: this function will be called when the character defeats the boss
    :postcondition: prints ASCII art on the screen about winning message
    """
    print(f"\033[1;35mThe Boss has been defeated!\033[0m. \n You have saved all the Pokemon!")
    print("")
    print("""\033[1;33m
    #     #                               #######                               
    #     #   ##   #####  #####  #   #    #       #    # #####  # #    #  ####  
    #     #  #  #  #    # #    #  # #     #       ##   # #    # # ##   # #    # 
    ####### #    # #    # #    #   #      #####   # #  # #    # # # #  # #      
    #     # ###### #####  #####    #      #       #  # # #    # # #  # # #  ### 
    #     # #    # #      #        #      #       #   ## #    # # #   ## #    # 
    #     # #    # #      #        #      ####### #    # #####  # #    #  ####  
                                                                             
    \033[0m""")


# Boss
def create_boss() -> dict:
    """Generate a boss dictionary containing information of the boss.

    :postcondition: boss dictionary has the key hp representing current health points
    :postcondition: boss dictionary has the key min_damage representing minimum damage can deal
    :postcondition: boss dictionary has the key max_damage representing maximum damage can deal
    :postcondition: boss dictionary has the key location representing boss's location
    :postcondition: boss' location is fixed at [5, 5]
    :return: information of the boss
    """
    boss = dict(hp=80,
                min_damage=15, max_damage=20,
                location=[5, 5])
    return boss


# Game logic
def is_boss_alive(boss: dict) -> bool:
    """Check if boss is still alive.

    :param boss: a dictionary containing the information of the boss
    :precondition: hp of the boss must be integer
    :precondition: character must contain correct boss status
    :postcondition: returns True when boss's hp is bigger than 0
    :postcondition: returns False when boss's hp is equal or smaller than 0
    :return: True for the boss is alive or False for the boss is dead
    >>> boss_dict = {'hp':30}
    >>> is_boss_alive(boss_dict)
    True
    >>> boss_dict = {'hp':0}
    >>> is_boss_alive(boss_dict)
    False
    """
    if boss["hp"] > 0:
        return True
    else:
        return False


def check_for_boss(character: dict, boss: dict) -> bool:
    """Check if the user encounters the boss.

    :param character: a dictionary containing character_status
    :param boss: a dictionary containing boss_status
    :precondition: character must contain correct character status
    :precondition: character must contain correct boss status
    :postcondition: returns True when the location of the boss and character are equal
    :postcondition: returns False when the location of the boss and character are not equal
    :return: True to encounter the boss and enter the combat or False to not encounter the boss

    >>> character_dict = {'location': [0, 0], 'min_damage':20, 'max_damage': 25, 'hp':20, 'level': 1, 'exp': 0}
    >>> boss_dict = {'location': [5, 5], 'hp': 30, 'min_damage':20, 'max_damage': 30}
    >>> check_for_boss(character_dict, boss_dict)
    False
    """
    if character["location"] == boss["location"]:
        print(r"""\
                            _.------.                        .----.__
                   /         \_.       ._           /---.__  
                  |  O    O   |\\___  //|          /       `\ |
                  |  .vvvvv.  | )   `(/ |         | o     o  \|
                  /  |     |  |/      \ |  /|   ./| .vvvvv.  |
                 /   `^^^^^'  / _   _  `|_ ||  / /| |     |  |
               ./  /|         | O)  O   ) \|| //' | `^vvvv'  |
              /   / |         \        /  | | ~   \          | 
              \  /  |        / \ Y   /'   | \     |          |   ~
               `'   |  _     |  `._/' |   |  \     7        /
                 _.-'-' `-'-'|  |`-._/   /    \ _ /    .    |
            __.-'            \  \   .   / \_.  \ -|_/\/ `--.|_
         --'                  \  \ |   /    |  |              `-
        After I'm through with you, I'm going to fuse you and your Pokemon into a brand new chimera!
        You'll make an excellent lap dog.
        """)
        combat_round_with_boss(character, boss)
        return True
    return False


def add_foe_difficulty_text(level: str):
    """Generate a colored description next the foe's name.

    :param level: the level of character which determines foe's strength
    :precondition level: level must be a string
    :precondition: this function must be used with map function
    postcondition: returns the line of code to print the colored description
    :return: the colored description of foe's strength
    """
    if level == "1":
        return f"\033[0;30;42m(Easy)\033[0m"  # easy foe
    if level == "2":
        return f"\033[0;30;43m(Medium)\033[0m"  # intermediate foe
    else:
        return f"\033[0;30;45m(Hard)\033[0m"  # difficult foe


def check_for_foe(character: dict, boss: dict) -> bool:
    """Check if the user encounters the foe.

    :param character:a dictionary containing character_status
    :param boss: a dictionary containing boss_status
    :precondition: the location of user must not be equal as the location of boss
    :precondition: character must contain correct character status
    :precondition: character must contain correct boss status
    :postcondition: character will heal no foe is encountered
    :postcondition: character can decide whether to continue fighting or flee
    :postcondition: returns False if character doesn't encounter a foe
    :postcondition: returns True if character encounter a foe
    :return: True to encounter a foe and enter the combat or False to not encounter a foe
    """
    if not character["location"] == boss["location"]:
        encounter_foe = create_foe(character)  # make a foe based on character level
        if not encounter_foe:  # if the user doesn't encounter a foe
            heal(character)  # the user will heal by 4 HP
            display_character_health(character)  # show character current HP
            return False
        else:
            print(f"\033[31mYou encounter {encounter_foe['name']}\033[00m", end='')

            # Add foe's power as assigning colors by mapping
            level = str(character["level"])
            for colored_level in map(add_foe_difficulty_text, level):
                print(colored_level, end='')
            print("")

            action = get_user_input("['k': enter combat] [else: run away]")

            if not action or combat_round(character, encounter_foe, action) == CHARACTER_DEAD():
                # If user type "quit" or the character died, return True to end the game
                return True


def play(character: dict, board: list, boss: dict) -> bool:
    """Get the command from the user to play and run the game.

    :param character: the game character created by the user
    :param board: a list containing 625 tuples which is 25X25 matrix
    :param boss: a dictionary containing the information of the boss
    :precondition: character must be a valid character dictionary
    :precondition: boss must be a valid boss dictionary
    :precondition: board must be a valid board list containing 625 tuples
    :return: True is the sign the game over, False is the sign to continue the game
    """
    # Ask user for direction to go

    direction = get_user_input("\033[1;36mWhich way would you like to go?:\033[0m")

    # If the direction input is not valid, return False and ask again
    if not direction:
        return False

    if move(character, direction, board):

        # Show the current location with printed map on the screen
        print_board(character)
        check_for_boss(character, boss)
        check_for_foe(character, boss)
    else:
        print("** Hey!! You can't go there! Please enter another command. **")
        return False


def game():
    """Drive the game and setup for basic elements to play game.

    :postcondition: ends the game when the user achieve the goal or the boss is dead or character dies,
    otherwise keep playing
    """

    opening_message()
    board = create_board()

    character = create_character()
    boss = create_boss()
    goal_achieved = False  # Game over when the goal is achieved

    # The game will be continue until the user achieves the goal
    while not goal_achieved and is_boss_alive(boss) and character["hp"] > 0:
        goal_achieved = play(character, board, boss)


def main():
    """Drives the program."""
    game()


if __name__ == "__main__":
    main()
