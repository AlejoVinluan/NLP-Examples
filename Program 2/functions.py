import re

def clean_data(arr):
    text = ' '.join(arr)
    text = text.lower()
    # Need to replace periods EXCEPT for when it's between numbers
    regex = r"(\d+(?:\.\d+))|\W+"
    text = re.sub(regex, lambda x: x.group(1) if x.group(1) else " ", text)
    return text.split(' ')

def get_lexical_diversity(arr):
    text = ' '.join(arr)
    return len(set(text)) / len(arr)