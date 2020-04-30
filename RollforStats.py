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
for key,value  in StartingStats.items(): # print the keys of StartingStats
    num = num + 1
    print("\n",num,"- {} ".format(key))
    count =  0  
    rolls = []  # create the list of roll results

    while count < 4:
        rolls.append(roll6())
        count += 1
    rolls.sort() # sort rolls into ascending order

    print("You rolled: ",rolls)
    rolls.pop(0) # drop the first (lowest) number in rolls

    total = 0
    for i in rolls: 
        total = total + i

    print("Your three highest rolls were {}, for a total of {}.".format(rolls,total))
    #### STUCK HERE ###
    #need to update the value of the dictionary key to the total variable
