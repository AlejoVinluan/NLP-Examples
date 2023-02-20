import copy
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from random import randint, seed

def pre_process(raw_text):
    # Tokenize the lowercase, raw text
    tokenized_lower = word_tokenize(raw_text.lower())

    # Reduce tokens to only alpha
    tokenized_arr = [word for word in tokenized_lower if word.isalpha()]

    # Remove any stopwords located in array
    english_stopwords = set(stopwords.words('english'))
    tokenized_arr = [word for word in tokenized_arr if word not in english_stopwords]

    # Remove any words with length less than or equal to 5
    tokenized_arr = [word for word in tokenized_arr if len(word) > 5]

    # Lemmatize Tokens
    tokenized_arr = [WordNetLemmatizer().lemmatize(word) for word in tokenized_arr]
    tokens_arr = copy.deepcopy(tokenized_arr)
    num_tokens = len(tokenized_arr)

    # Create a set of tokens to ensure uniqueness
    tokenized_arr = set(tokenized_arr)
    
    # POS-Tag the lemmas and print the first 20 tagged
    pos_tagged_arr = pos_tag(tokenized_arr)
    print("Part of Speech Tagged Lemmas (first 20) - ")
    print(pos_tagged_arr[:20],"\n")

    # Extract all nouns
    nouns = [noun[0] for noun in pos_tagged_arr if noun[1] == "NN"]
    num_nouns = len(nouns)

    # Print the number of tokens and the number of nouns
    print("Number of tokens:", num_tokens)
    print("Number of nouns:", num_nouns, "\n")

    # Return the tokens and the nouns
    return tokens_arr, nouns

# Prints letters if letters have been guessed
# Prints underscore if letters have not been guessed
def printState(word, guess, points):
    for c in word:
        if c in guess:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print('\n')
    # Prints total points
    print("Point total:", points, '\n')
    return

# Word game!
def word_game(word_list):
    # Select a random word from word_list
    word = word_list[randint(0,len(word_list)-1)]

    print("Starting the Word Guessing Game!")
    print("Guess a word with", len(word), "letters.\n")

    # Start the player with 5 points
    points = 5

    # Create a set to add letters that have already been guessed
    alreadyGuessed = set()

    # Print initial state
    printState(word,alreadyGuessed,points)

    # Maintain the game while player has more than 5 points
    while points >= 0:
        # Ask user for a guess
        guess = input('Guess a letter: ').lower()
        print()

        # Verify that the guess is 1 letter
        if len(guess) != 1 or not guess.isalpha():
            print("Make sure your guess is only 1 letter and is a letter.\n")
            continue

        # Check if user quits the game
        if guess == '!':
            print("Detected `!`. Ending game.\n")
            print("The word was", word)
            break

        # Check that letter is in word and if letter hasn't been guessed yet
        if guess in word and guess not in alreadyGuessed:
            print("Right!")
            alreadyGuessed.add(guess)
            # Add a point
            points += 1
            printState(word,alreadyGuessed,points)
        # Edge case in case user guesses a letter they have already used
        elif guess in word and guess in alreadyGuessed:
            print("You already guessed this letter.")
            points -= 1
            printState(word,alreadyGuessed,points)
        # Instance in which the lettter guess is wrong
        else:
            print("Sorry, guess again.")
            points -= 1
            printState(word,alreadyGuessed,points)
        
        # Check win condition
        if len(alreadyGuessed) == len(set(word)):
            print("You've guessed the word!")
            break
    
    # Print the following once game ends
    print("Game ended.")
    # Check if user lose condition was met
    if points < 0:
        print("The word was", word)
    print("Total Points:",points)

