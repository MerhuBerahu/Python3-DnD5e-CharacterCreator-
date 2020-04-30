import random 

"""
You generate your character’s six ability scores randomly. 
Roll four 6-sided dice and record the total of the highest 
three dice on a piece of scratch paper. Do this five more 
times, so that you have six numbers.
"""

def roll6():
    number = random.randint(1,6)
    return number

StartingStats = {'Strength': 0,'Dexterity': 0,'Constitution':0 ,'Intelligence':0 ,'Wisdom': 0, 'Charisma': 0}

num = 0
for key,value  in StartingStats.items(): # print the keys and values of PBStartingStats
    num = num + 1
    print(num,"- {} = {}".format(key, value))
    print("your rolls were: ")
    count =  0
    while count < 4:
        rolls = (roll6())
        print(" you rolled a ",rolls)
        count += 1
        print("Your three highest rolls were {}, for a total of {}.")