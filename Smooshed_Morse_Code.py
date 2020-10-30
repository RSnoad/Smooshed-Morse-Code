
morsecodetranslation = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
"i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
"s":"...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}

# Translate English alphabet to morse code with no spaces.
def smooshedmorse(stringtotranslate):
    stringtotranslate = stringtotranslate.lower()
    translatedstring = ""

    for i in range(len(stringtotranslate)):
        translatedstring += morsecodetranslation.get(stringtotranslate[i:i+1], "\n")

    return translatedstring


