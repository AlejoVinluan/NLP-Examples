import requests
import random
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

# Returns a soup object of a given url
def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')

# Returns 1 list of 15 total URL's
def scrape_base(url):
    soup = get_soup(url)
    base_url = url.split("/")[2]

    # Gets different links within the Wikipedia page
    stat_links = soup.find_all('a')
    wiki_links = set()
    external_links = set()
    for raw_link in stat_links:
        link = raw_link.get('href')
        # Filter for websites that don't work well in this assignment
        if not link or 'file' in link.lower() or link.startswith('#') or 'archive' in link.lower() or 'slate' in link.lower():
            continue
        if link.startswith('/wiki/'):
            wiki_links.add('https://' + base_url + link)
        elif 'wiki' not in link.lower() and link.lower().startswith('https://'):
            external_links.add(link)
    return create_list(wiki_links, external_links)
        
# Creates a 15 sized sample from two lists, 10 from list1, 5 from list2
def create_list(list1, list2):
    random.seed(123)
    main_list = random.sample(sorted(list1),10)
    list2_sample = random.sample(sorted(list2),5)
    for sample in list2_sample:
        main_list.append(sample)
    return main_list

# Makes a file for the url inputted
def extract_and_make_file(url, file_name):
    soup = get_soup(url)
    text = soup.get_text()
    with open("text_files/" + file_name, "w", encoding="utf-8") as file:
        file.write(text)
    
# Clean up text. Extract from NLTK tokenizer
def clean_up_text(file):
    clean_text = ""
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            if not line.isspace():
                clean_text += line
    tokenized_sentences = sent_tokenize(clean_text)
    final_text = ""
    for sentence in tokenized_sentences:
        final_text = final_text + sentence + "\n"
    file_name = file.split('/')[1]
    # Write to a new file in clean_files directory
    with open("clean_files/clean_" + file_name, 'w', encoding="utf-8") as f:
        f.write(final_text)

        
def extract_terms(file_directory):
    clean_file_dir = os.listdir(file_directory)
    filtered_words = []
    # Loop through each file and add all words to filtered_words array
    for file in clean_file_dir:
        raw_arr = []
        with open(file_directory + "/" + file, 'r', encoding="utf-8") as f:
            raw_arr = f.readlines()
        raw_text = " ".join(raw_arr)
        tokenized_words = word_tokenize(raw_text.lower())
        stop_words = set(stopwords.words('english'))
         # Lower case and remove stopwords
        filtered_arr = [word for word in tokenized_words if word.isalpha() and word not in stop_words and len(word) > 1]
        for word in filtered_arr:
            filtered_words.append(word)
            
        # Find frequency of all words
        word_frequency = {}
        for word in filtered_words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    # Sort the words in dict by frequency, with count descending
    sorted_words = sorted(word_frequency.items(), key=lambda x:x[1], reverse=True)
    # Return first 40 words of dict
    return sorted_words[:40]
    