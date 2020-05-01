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


