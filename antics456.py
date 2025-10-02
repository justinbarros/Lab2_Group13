import string

def is_palindrome(string):
  '''Check if the word is palindrome, a word, phrase, 
  or sequence that reads the same backward as forward,'''

  #convert the string to lower case
  string = string.lower()

  # Using slice it will compare the reverse string and return true if palendrom and fale if not
  return string == string[::-1]

def is_pangram(sentence):
  ''' Check if the user's given phrase or sentence is pangram. Pangram if all letters in the alphabet is present'''

  # Convert the user input sentence to lower for case sensitivity
  sentence = sentence.lower()

  # Get all the lower characters in alphabet
  alphabet = string.ascii_lowercase

  for char_code in alphabet:
    if char_code not in sentence:
      return False # If one letter in alphabet is missing in the sentence
  return True # If all letters in alphabet is present

def is_tautogram(text):
  text = text.lower().split() # Convert to lower case and split the given text to list of words.

  first_letter = text[0][0] # Get the first letter of evey singe word.

  for word in text:
    if word[0] != first_letter:
      return False # If any word does not have the same letter
    
  return True # if all words start with the same letter



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
