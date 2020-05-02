#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""You have 27 points_left to spend on your ability scores. 
The cost of each score is shown on the Ability Score Point 
Cost table. For example, a score of 14 costs 7 points. 
Using this method, 15 is the highest ability score you can 
end up with, before applying racial increases. You can’t 
have a score lower than 8.
"""
#TODO stuff1


def check_input():
    '''Check if an input is and integer(not a chr/str) within a specific range'''

    min_value = 1
    max_value = 6
    while True:
        try:
            intTarget = int(input(""))
        except ValueError:
            print("That's not a valid Selection")
            continue
        else:
            if intTarget < min_value or intTarget > max_value:
                print("That's not a valid Selection")
                continue
            else:
                return (intTarget)


def buy_stats():
    """Spend points to increase stats"""

    PBStartingStats = {'Strength': 8, 'Dexterity': 8, 'Constitution': 8, 'Intelligence': 8, 'Wisdom': 8, 'Charisma': 8}

    points_left = 27

    print("You have 27 points_left to spend on your ability scores. The cost of each score is shown on the Ability Score Point Cost table. For example, a score of 14 costs 7 points_left. Using this method, 15 is the highest ability score you can end up with, before applying racial increases. You can’t have a score lower than 8.")
    while points_left > 0:
        print("\nWhich Stat do you want to increase?")

        num = 0
        for key,value in PBStartingStats.items(): # print the keys and values of PBStartingStats
            num += 1
            print(F"{num} - {key} = {value}")
            
        selection = check_input() # sends users input to check_input() to ensure its a valid option
        print("\npoints_left left = ", points_left) # Prints points_left left
        if selection == 1:
            if PBStartingStats["Strength"] == 15: # checks that stat isn't at Maximum
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Strength"] += 1 # add a point to the selected stat and subtract from points_left
                points_left -= 1
        elif selection == 2:
            if PBStartingStats["Dexterity"] == 15:
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Dexterity"] += 1 
                points_left -= 1
        elif selection == 3:
            if PBStartingStats["Constitution"] == 15:
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Constitution"] += 1 
                points_left -= 1
        elif selection == 4:
            if PBStartingStats["Intelligence"] == 15:
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Intelligence"] += 1 
                points_left -= 1
        elif selection == 5:
            if PBStartingStats["Wisdom"] == 15:
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Wisdom"] += 1 
                points_left -= 1
        elif selection == 6:
            if PBStartingStats["Charisma"] == 15:
                print("You cant add any more points_left here, you have reached the maximum")
                continue
            else:
                PBStartingStats["Charisma"] += 1 
                points_left -= 1

    print("You're starting stats are:")
    for key, value  in PBStartingStats.items():  # print the keys and values of PBStartingStats
        num = num + 1
        print(F"{num} - {key} = {value}")

    print("are you happy with these?")
 
    while True:  # Check input Validity
        validYes = ('y', 'Y', 'yes', 'Yes', 'YES', 'yeah')
        ValidNo = ('n', 'N', 'NO', 'no', 'No')
        redo = input("Type 'Y' to continue or 'N' to start over: > ")
        if redo in validYes:
            print("Continuing to rest of program")  # placeholder
        elif redo in ValidNo:
            buy_stats()
    else:
        print('Sorry But You Didnt Choose a valid option... Try Again')
        


#testing
buy_stats()
