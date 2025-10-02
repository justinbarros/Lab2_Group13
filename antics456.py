
def isogram(word):
    '''checks if a word is an isogram,
    a word in which no letter occurs more than once.
    It takes a word as an input and returns True or False.'''
    word = word.lower()
    used = []

    for letter in word:
        if letter in used:
            return False
        else:
            used.append(letter)
    
    return True

def abecedarian(word):
    '''checks if a word is an abecedarian,
    a word in which the letters occur in alphabetical order.
    It takes a word as an input and returns True or False.'''
    word = word.lower()
    i = 0

    while i < len(word) - 1:
        current = word[i]
        next = word[i + 1]

        if ord(current) > ord(next):
            return False

        i = i + 1

    return True

def doubloon(word):
    '''checks if a word is a doubloon,
    a word in which every letter in a word appears exactly twice.
    It takes a word as an input and returns True or False.'''
    word = word.lower()
    checked = []

    for letter in word:
        if letter not in checked:
            count = 0

            for l in word:
                if l == letter:
                    count = count + 1
            
            if count != 2:
                return False

            checked.append(letter)
    
    return True
