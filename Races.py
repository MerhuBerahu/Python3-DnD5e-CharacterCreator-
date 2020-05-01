#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Display race information and select a race
"""


import json
from Systems import check_input

def race_info():
    """Pull in race information from a Json, format it into a list for 
selection and make a choice. Then print the values of that race
from the Json
"""
    with open("Jsons\\races.json", encoding="utf8") as test:  #Open races.json as test
        race_list = json.load(test)

    print("Which Race would you like to know more about?")

    race_choices = {}
    for index, item in enumerate(race_list, 1):
        print(index, item)  #Print Numbers list of items in races.json
        dict1 = {index:item}  #create dict with enumerate number(index) as a key and item as the value
        race_choices.update(dict1)

    selection = check_input(1, 2)
    if selection in race_choices:
        chosen_race = race_choices[selection]
        for i in race_list[chosen_race].values():
            print(i,"\n")

race_info()