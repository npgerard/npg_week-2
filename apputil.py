import numpy as np


# update/add code below ...

def ways(total_cents):
    '''returns the number of ways to make change for total_cents using only nickels and pennies'''

    # iniitialize the counter at 0
    combintation_count = 0

    #initialize the nickel counter at 0
    nickel_count = 0

    # what are the maximum number of nickels?
    max_nickels = total_cents // 5

    # using range() start with 0 nickels and pennies = total_cents, 
    # then increment nickels by 1 and then pennies = total_cents - (nickel_count * 5)
    for nickel_count in range(max_nickels + 1):      # +1 to include max_nickels whereaas range() excludes the end value
        penny_count = total_cents - (nickel_count * 5)
        if penny_count >= 0:
            combintation_count += 1

    return combintation_count


print(ways(1003)) 


def lowest_score(names, scores):
    '''returns the name with the lowest score based on the first argument containing an np array of names
    and the second argument containing an np array of scores'''
    # argmin returns the index of the minimum value in an array.
    # By passing that index to names, we get the name with the lowest score.
    return names[np.argmin(scores)]

print(
    lowest_score(
        np.array(["Trixie", "Jimbo", "Raja", "Katya", "Jasmine", "Ginger"])
        ,np.array([98, 87, 92, 91, 85, 93])
        )
    )

def sort_names(names, scores):
    '''returns an array sorted by the scores in descending orders'''

    #create the array to be sorted
    key_value_pair = np.stack((names, scores), axis=1)

    #sort the array by the scores in descending order
    sorted_array = key_value_pair[key_value_pair[:, 1].argsort()[::-1]]

    return sorted_array

print(
    sort_names(
        np.array(["Trixie", "Jimbo", "Raja", "Katya", "Jasmine", "Ginger"])
        , np.array([98, 87, 92, 91, 85, 93])
        )
    )


print("hi")