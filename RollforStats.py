#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""You generate your character’s six ability scores randomly. 
Roll four 6-sided dice and record the total of the highest 
three dice on a piece of scratch paper. Do this five more 
times, so that you have six numbers.
"""

import random

def roll6():
    """Creates a random int between 1 and 6"""
    number = random.randint(1,6)
    return number

def stats_roll():
    """ creates 4 random int's between 1 and 6 for each
    items in starting_stats, dops the lowest and calculates
    the total
    """
    starting_stats = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0}

    num = 0
    for key, value  in starting_stats.items():  # print the keys of starting_stats
        num = num + 1
        print(F"\n", num, "- {key} ")
        count = 0  
        rolls = []  # create the list of roll results

        while count < 4:
            rolls.append(roll6())
            count += 1
        rolls.sort()  # sort rolls into ascending order

        print(F"You rolled: {rolls}")
        rolls.pop(0)  # drop the first (lowest) number in rolls

        total = 0
        for i in rolls:
            total = total + i

        print("Your three highest rolls were {}, for a total of {}.".format(rolls, total))
        starting_stats[key] = total

    print("\n\nYor stats are:\n")
    for key, value in starting_stats.items():  # print the keys and values of starting_stats
        print(F"{key} = {value}")

#Testing
stats_roll()