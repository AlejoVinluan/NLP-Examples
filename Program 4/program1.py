import pickle
from nltk import bigrams
from nltk.tokenize import word_tokenize

class Main:
    def read_file(file_path):
        try:
            f = open(file_path, 'r', encoding='utf-8')
            raw_arr = f.readlines()
            f.close()
        except:
            print("Could not find file", file_path)
            exit(1)
        
        raw_text = ' '.join(raw_arr)
        raw_text.replace('\n', '')
    
        tokenized_text = word_tokenize(raw_text)
    
        # Bigrams
        bigram_tokens = list(bigrams(tokenized_text))
    
        # Unigrams
        unigram_tokens = list(tokenized_text)
    
        # Create dictionary of counts for bigrams
        bigram_dict = {}
        for token in bigram_tokens:
            if token in bigram_dict:
                bigram_dict[token] += 1
            else:
                bigram_dict[token] = 1
                
        # Create dictionary of counts for unigram
        unigram_dict = {}
        for token in unigram_tokens:
            if token in unigram_dict:
                unigram_dict[token] += 1
            else:
                unigram_dict[token] = 1
        return unigram_dict, bigram_dict
    
    english_unigram, english_bigram = read_file('data/LangId.train.English')
    french_unigram, french_bigram = read_file('data/LangId.train.French')
    italian_unigram, italian_bigram = read_file('data/LangId.train.Italian')
    
    pickle.load(english_unigram, open('english_unigram.p', 'wb'))
    pickle.dump(english_bigram, open('english_bigram.p', 'wb'))
    pickle.dump(french_unigram, open('french_unigram.p', 'wb'))
    pickle.dump(french_bigram, open('french_bigram.p', 'wb'))
    pickle.dump(italian_unigram, open('italian_unigram.p', 'wb'))
    pickle.dump(italian_bigram, open('italian_bigram.p', 'wb'))
        
    

    
    
    
