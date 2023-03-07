import requests
import random
import os
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
        if not link or 'file' in link.lower() or link.startswith('#'):
            continue
        if link.startswith('/wiki/'):
            wiki_links.add('https://' + base_url + link)
        elif 'wiki' not in link.lower() and link.lower().startswith('https://'):
            external_links.add(link)
    return create_list(wiki_links, external_links)
        
# Creates a 15 sized sample from two lists, 10 from list1, 5 from list2
def create_list(list1, list2):
    random.seed(123)
    main_list = random.sample(list1,10)
    list2_sample = random.sample(list2,5)
    for sample in list2_sample:
        main_list.append(sample)
    return main_list

# Makes a file for the url inputted
def extract_and_make_file(url, file_name):
    soup = get_soup(url)
    text = soup.get_text()
    with open("text_files/" + file_name, "w") as file:
        file.write(text)
    
# Clean up text. Extract from NLTK tokenizer
def clean_up_text(file):
    with open(file, 'r') as f:
        text_arr = f.readlines()
    main_text = ""
    for text in text_arr:
        text.strip()
        if len(text) > 0:
            main_text = main_text + text
    print(main_text)
    with open(file, 'w') as f:
        f.write(main_text)
        
# Extract 3 important terms from file
def extract_terms(file):
    # Lower case and remove sotpwords
    
    return 0
    