import json


def check_input(min_value, max_value):
    '''Check if an input is and integer(not a chr/str) within a specific range'''

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

with open("Jsons\\races.json", encoding="utf8") as test:  #open races.json as test
    race = json.load(test)

print("Which Race would you like to know more about?")

races = {}
for index, item in enumerate(race, 1):
    print(index, item)  #Print Numbers list of items in races.json
    dict1 = {index:item}
    races.update(dict1)

selection = check_input(1, 2)
if selection in races:
    chosen_race = races[selection]
    print(race_list[chosen_race].keys())
    print(race_list[chosen_race].items())
    print(race_list[chosen_race].values())
    


print("Which Race would you like to know more about?")

num = 0
races = {}
for item in race:
    num += 1
    dict1 = {num: item}
    races.update(dict1)
    print(F"{num} - {item}")

selection = check_input(1, 2)
if selection in races:
    chosen_race = races[selection]
    print(race_list[chosen_race].keys())
    print(race_list[chosen_race].items())
    print(race_list[chosen_race].values())




