# Detect English module
# Forked from http://inventwithpython.com/hacking (BSD licensed).

# To use:
# import detectEnglish
# detectEnglish.isEnglish(someString) returns true or false.
# A "dictionary.txt" file is required in this directory with one English
# word per line.

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    # Return 0.0 if no possible words.
    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches +=1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must be in the dictionary file, and
    # 85% of characters in the message must be letters or spaces.
    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch






