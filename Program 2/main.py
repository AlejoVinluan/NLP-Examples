from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from functions import pre_process

class Main:
    # Read anat19.txt file
    f = open('data/anat19.txt', 'r')
    raw_arr = f.readlines()
    f.close()
    raw_text = ' '.join(raw_arr)

    # Tokenize the provided raw text
    tokenized_arr = word_tokenize(raw_text)
    
    # Calculate lexical diversity
    #  lexical diversity = unique tokens / total tokens
    print("Lexical diversity:", "{:.2f}".format(len(set(tokenized_arr)) / len(tokenized_arr)),"\n")

    tokens, nouns = pre_process(raw_text)