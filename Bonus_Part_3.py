from Smooshed_Morse_Code import smooshedmorse
from Word_List import wordlistasstring


listofwords = wordlistasstring.split()

# Function that returns a list of words from wordlist that are of the specified length.
def findWordsOfSpecifiedLength(n):
    specifiedlengthlong = []
    for i in range(len(listofwords)):
        if len(listofwords[i]) == n:
            specifiedlengthlong.append(listofwords[i])

    return specifiedlengthlong


# Translate a list of words as opposed to a long string as before. Returns the translations as a list.
def translatelist(listtotranslate):
    translatedlist = []
    for i in range(len(listtotranslate)):
        translatedlist.append(smooshedmorse(listtotranslate[i]))

    return translatedlist


# Probably extract functions to cut this down, unsure exactly where to split.
# Function takes length of words to check as input and returns a list of perfectly balanced translations, with
# English also.
def findPerfectlyBalancedWords(lengthofword):
    englishlist = findWordsOfSpecifiedLength(lengthofword)
    listtocheck = translatelist(englishlist)
    balancedwords = []

    for listiterator in range(len(listtocheck)):
        dotcount = 0
        dashcount = 0

        for stringiterator in range(len(listtocheck[listiterator])):
            if listtocheck[listiterator][stringiterator] == ".":
                dotcount += 1
            elif listtocheck[listiterator][stringiterator] == "-":
                dashcount += 1
        if dotcount == dashcount:
            balancedwords.append(tuple((listtocheck[listiterator], englishlist[listiterator])))

    return balancedwords


print(findPerfectlyBalancedWords(21))

