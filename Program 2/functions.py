import re

def cleanData(text):
    # Need to replace periods EXCEPT for when it's between numbers
    return re.sub("[^a-zA-Z0-9 .,]|(?<!\\d)[.,]|[.,](?!\\d)", "", text)

def getLexicalDiversity(text):
    return len(set(text)) / len(text)