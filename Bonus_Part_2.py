from Smooshed_Morse_Code import smooshedmorse
from Word_List import wordlistasstring

# Find the only word that has 15 dashes in a row.

listofwords = wordlistasstring.split()

# Find the first translated word that contains the specified string.
def isStringInTranslatedList(stringtofind):

    # Fiddled around with having for i in listofwords as well(instead of range(len()), not sure which is better,
    # nor which one I prefer.
    for i in range(len(listofwords)):
        if stringtofind in smooshedmorse(listofwords[i]):
            return listofwords[i]


