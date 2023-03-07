import os
from functions import scrape_base, extract_and_make_file, clean_up_text

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
    for link in link_set:
        file_name = "file" + str(idx) + ".txt"
        extract_and_make_file(link, file_name)
        idx += 1

    text_files_dir = os.listdir('text_files')
    clean_up_text("text_files/file0.txt")
    #for file_name in text_files_dir:
        #clean_up_text("text_files/" + file_name)
    


    
    
    
