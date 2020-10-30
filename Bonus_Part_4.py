from Smooshed_Morse_Code import smooshedmorse
from Word_List import wordlistasstring

# Function that checks if a string is a palindrome.
def isPalindrome(stringtocheck):
    return stringtocheck == stringtocheck[::-1]

# Function that takes the length of the strings to check as input and returns the first word that is of specified
# length and has a morse translation that is a palindrome.
def isPalindromeInList(palindromelength):
    listofwords = wordlistasstring.split()
    for i in range(len(listofwords)):
        if isPalindrome(smooshedmorse(listofwords[i])) and len(listofwords[i]) == palindromelength:
            return listofwords[i]

print(isPalindromeInList(13))
print(smooshedmorse("intransigence"))
