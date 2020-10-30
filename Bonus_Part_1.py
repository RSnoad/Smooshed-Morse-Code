from Word_List import wordlistasstring
from Smooshed_Morse_Code import smooshedmorse


# Find the only morse code sequence that's the code for 13 different words.

# Tests take half a second longer if this is declared in the function - no idea why.
# This variable is repeated a lot over the exercises., not sure where is best to put it
translatedwords = smooshedmorse(wordlistasstring).split()


def codethatappears(n):

    listofkeys = []
    counted = dict()

    # Loop that creates dictionary with morse code as key and number of instances as value.
    # Can also use Counter from collections import for this part.
    # Extract function if find time?
    for i in translatedwords:
        counted[i] = counted.get(i, 0) + 1

    # Loop that creates a list of codes that appear a specified number of times.
    for key, value in counted.items():
        if value == n:
            listofkeys.append(key)

    return listofkeys


print(codethatappears(13))

# -....--.... appears 13 times