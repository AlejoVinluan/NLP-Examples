import os
import pickle
from functions import scrape_base, extract_and_make_file, clean_up_text, extract_terms

class Main:
    # Start with the main website
    nba_wiki = 'https://en.wikipedia.org/wiki/National_Basketball_Association'

    # Create a set of links extracted from main website
    link_set = scrape_base(nba_wiki)
    
    # Make a subdirectory for the created files
    if not os.path.exists("text_files"):
        os.makedirs("text_files")

    # Extract all text from a webpage and store text in file
    #  idx used to create unique filename for text
    idx = 0

    # Create a file for each link from original website
    for link in link_set:
        file_name = "file" + str(idx) + ".txt"
        extract_and_make_file(link, file_name)
        idx += 1
        
    # Create directory if it does not exist
    if not os.path.exists("clean_files"):
        os.makedirs("clean_files")
    
    # Clean text from all text files originally created
    text_files_dir = os.listdir('text_files')
    for file_name in text_files_dir:
        clean_up_text("text_files/" + file_name)
        
    # Extract the important terms from the cleaned files
    important_terms = extract_terms("clean_files/")
    # Print the important terms and their occurence
    for idx, term in enumerate(important_terms):
        print("Rank:", idx+1)
        print("Term:", term[0])
        print("Occurrences:", term[1], "\n")
    
    # Create a knowledge base from the top 10 terms by hand
    knowledge_base = {
        "team": "a group of players forming one side in a competitive game or sport",
        "league": "a collection of people, countries, or groups that combine for a particular purpose, typically mutual protection or cooperation",
        "nba": "the National Basketball Assosciation",
        "season": "a fixed time in the year when a particular sport is played",
        "wnba": "the Womens National Basketball Assosciation",
        "players": "a person taking part in a sport or game",
        "basketball": "a game played between two teams of five players in which goals are scored by throwing a ball through a netted hoop fixed above each end of the court",
        "sport": "an activity involving physical exertion and skill in which an individual or team competes against another or others for entertainment",
        "game": "a form of play or sport, especially a competitive one played according to rules and decided by skill, strength, or luck",
        "may": "The month where the NBA Playoffs and NBA Finals generally occur"
    }
    
    # Print each key and definition of the knowledge base
    for key in knowledge_base:
        print("Term:", key)
        print("Definition:", knowledge_base[key], "\n")
    
    # Create a pickle of the dictionary for the knowledge base
    pickle.dump(knowledge_base, open('knowledge_base.p', 'wb'))


    
    
    
