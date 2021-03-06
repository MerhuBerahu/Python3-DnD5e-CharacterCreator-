#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Display race information and select a race
"""
#TODO stuff


import json
from Systems import check_input

with open("Jsons\\races.json", encoding="utf8") as test:  #Open races.json as test
    race_list = json.load(test)

def race_info():
    """Pull in race information from a Json, format it into a list for 
selection and make a choice. Then print the values of that race
from the Json
"""
    print("Which Race would you like to know more about?")

    race_choices = {}
    for index, item in enumerate(race_list, 1):
        print(index, item)  #Print Numbers list of items in races.json
        dict1 = {index:item}  #create dict with enumerate number(index) as a key and item as the value
        race_choices.update(dict1)

    minmax = list(race_choices.keys())[0:]
    selection = check_input(minmax[0],minmax[1])
    if selection in race_choices:
        chosen_race = race_choices[selection]
        for i in race_list[chosen_race].values():
            print(i,"\n")
        choice = input("Type 'back' to go back to the race menu to look at another Race 1or 'continue' if you are happy to choose a race now.\n")
        if choice in ("back", "Back", "b", "B"):
            race_info()
        elif choice in ("continue", "continue"):
            race_selection()


def race_selection():
    print("Which Race would you like to be?")

    race_choices = {}
    for index, item in enumerate(race_list, 1):
        print(index, item)  #Print Numbers list of items in races.json
        dict1 = {index:item}  #create dict with enumerate number(index) as a key and item as the value
        race_choices.update(dict1)
    minmax = list(race_choices.keys())[0:]
    selection = check_input(minmax[0],minmax[1])
    if selection in race_choices:
        chosen_race = race_choices[selection]
    print(chosen_race)
    return chosen_race 

race_info()