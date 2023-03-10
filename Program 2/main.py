import sys
from nltk.tokenize import word_tokenize
from functions import pre_process, word_game

class Main:
    if len(sys.argv) <= 1:
        print("Please use the program by using:")
        print("python Main.py <file.txt>")
        exit(1)

    # Read File
    raw_arr = []
    try:
        f = open(sys.argv[1], 'r')
        raw_arr = f.readlines()
        f.close()
    except:
        print("Could not find file", sys.argv[1])
        exit(1)

    raw_text = ' '.join(raw_arr)

    # Tokenize the provided raw text
    tokenized_arr = word_tokenize(raw_text)
    
    # Calculate lexical diversity
    #  lexical diversity = unique tokens / total tokens
    print("Lexical diversity:", "{:.2f}".format(len(set(tokenized_arr)) / len(tokenized_arr)),"\n")

    # Pre-process the text and get tokens & nouns
    tokens, nouns = pre_process(raw_text)

    # Create a dictionary of nouns by
    dictionary = {}
    for noun in tokens:
        if noun in dictionary:
            dictionary[noun] += 1
        else:
            dictionary[noun] = 1

    # Sort the dictionary by descending order of occurence
    sorted_dict = sorted(dictionary.items(), key = lambda x: x[1], reverse=True)

    word_list = []
    for word, occurence in sorted_dict[:50]:
        word_list.append(word)
    
    # Play word game utilizing the first 50 values of the sorted dict
    word_game(word_list)
