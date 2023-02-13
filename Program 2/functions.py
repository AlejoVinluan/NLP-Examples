import copy
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

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

    print("Number of tokens:", num_tokens)
    print("Number of nouns:", num_nouns)

    return tokens_arr, nouns
