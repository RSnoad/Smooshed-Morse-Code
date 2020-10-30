from Smooshed_Morse_Code import smooshedmorse
from Bonus_Part_1 import codethatappears
from Bonus_Part_2 import isStringInTranslatedList
from Bonus_Part_3 import findWordsOfSpecifiedLength
from Bonus_Part_3 import findPerfectlyBalancedWords
from Bonus_Part_4 import isPalindrome
from Bonus_Part_4 import isPalindromeInList
from Word_List import wordlistasstring
import pytest


@pytest.mark.parametrize("test_input, expected", [("sos", "...---..."), ("daily", "-...-...-..-.--")])
def test_CanTranslateLowerCaseWords(test_input, expected):
    assert smooshedmorse(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("PROGRAMMER", ".--..-.-----..-..-----..-."), ("BiTs", "-.....-...")])
def test_CanCovertUpperCaseLettersToLowerCaseMorse(test_input, expected):
    assert smooshedmorse(test_input) == expected

# No longer TDD after this point, test created after code to allow for refactor.

def test_TranslatedWordListIsOfCorrectLengthIncludingNewLines():
    assert len(smooshedmorse(wordlistasstring)) == 4237061


@pytest.mark.parametrize("test_input, expected", [(4, "-...-....-.--."), (13, "-....--....")])
def test_BonusPart1CanFindCodeThatIsRepeatedASpecifiedNumberOfTimes(test_input, expected):
    assert expected in codethatappears(test_input)


@pytest.mark.parametrize("test_input, expected", [("-" * 14, "autotomous"), ("-" * 15, "bottommost")])
def test_BonusPart2CanFindATranslationWithSpecifiedString(test_input, expected):
    assert isStringInTranslatedList(test_input) == expected


def test_BonusPart3CanExtractWordsOfSpecifiedLength():
    listofwordslength21 = findWordsOfSpecifiedLength(21)
    assert all(len(listofwordslength21[i]) == 21 for i in range(len(listofwordslength21)))


def test_BonusPart3CanFindPerfectlyBalancedTranslations():
    assert("-.-.---..--.-..-.-...------....-.-..--..----....","counterdemonstrations") in findPerfectlyBalancedWords(21)


@pytest.mark.parametrize("test_input", [".--..-.----.-.-.----.-..--.", "level", "repaper", "step on no pets"])
def test_BonusPart4CanValidatePalindrome(test_input):
    assert isPalindrome(test_input)

@pytest.mark.parametrize("test_input", [".-..-.-.------...", "..-----", "some words"])
def test_BonusPart4CanRejectNonPalindrome(test_input):
    assert not isPalindrome(test_input)

def test_BonusPart4CanFindTheOnlyPalindromicTranslationOfLength13():
    assert isPalindromeInList(13) == "intransigence"



