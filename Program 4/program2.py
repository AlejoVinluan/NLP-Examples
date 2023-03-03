import pickle
from nltk import bigrams
from nltk.tokenize import word_tokenize

class Main:
    # English dictionaries
    english_unigram = pickle.load(open('english_unigram.p', 'rb'))
    english_bigram = pickle.load(open('english_bigram.p', 'rb'))
    # French Dictionaries
    french_unigram = pickle.load(open('french_unigram.p', 'rb'))
    french_bigram = pickle.load(open('french_bigram.p', 'rb'))
    # Italian Dictionaries
    italian_unigram = pickle.load(open('italian_unigram.p', 'rb'))
    italian_bigram = pickle.load(open('italian_bigram.p', 'rb'))
      
    def compute_probability(line, unigram_dict, bigram_dict, N, V):

        line_unigram = word_tokenize(line)
        line_bigram = list(bigrams(line_unigram))

        p_gt = 1
        p_laplace = 1
        
        for bigram in line_bigram:
            n = bigram_dict[bigram] if bigram in bigram_dict else 0
            n_gt = bigram_dict[bigram] if bigram in bigram_dict else 1/N
            d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
            if d == 0:
                p_gt = p_gt * (1 / N)
            else:
                p_gt = p_gt * (n_gt / d)
            p_laplace = p_laplace * ((n+1) / (d+V))
        
        return p_laplace

    
    # Calculate number of total tokens
    english_tokens = 0
    for word in english_unigram:
        english_tokens += english_unigram[word]
    english_vocab_size = len(english_unigram)
        
    french_tokens = 0
    for word in french_unigram:
        french_tokens += french_unigram[word]
    french_vocab_size = len(french_unigram)
        
    italian_tokens = 0
    for word in italian_unigram:
        italian_tokens += italian_unigram[word]
    italian_vocab_size = len(italian_unigram)
        
    try:
        f = open('data/LangId.test', 'r', encoding='utf-8')
        raw_arr = f.readlines()
        f.close()
    except:
        print("Could not find file", 'data/LangId.test')
        exit(1)
        
    f = open('output.txt', 'w')
    solution_arr = []
    
    for statement in raw_arr:
        english_prob = compute_probability(statement,english_unigram,english_bigram,english_tokens,english_vocab_size)
        french_prob = compute_probability(statement,french_unigram,french_bigram,french_tokens,french_vocab_size)
        italian_prob = compute_probability(statement,italian_unigram,italian_bigram,italian_tokens,italian_vocab_size)
        max_prob = max(english_prob, french_prob, italian_prob)
        
        if max_prob == english_prob:
            f.write("English\n")
            solution_arr.append("English")
        elif max_prob == french_prob:
            f.write("French\n")
            solution_arr.append("French")
        else:
            f.write("Italian\n")
            solution_arr.append("Italian")
    
    f.close()
    
    try:
        f = open('data/LangId.sol', 'r', encoding='utf-8')
        raw_ans = f.readlines()
        f.close()
    except:
        print("Could not find file", 'data/LangId.test')
        exit(1)
    
    idx = 0
    correct_answer = 0
    wrong_arr = []
    for answer in raw_ans:
        true_language = answer.split(" ")[1]
        if solution_arr[idx] in true_language:
            correct_answer += 1
        else:
            wrong_arr.append(idx)
        idx += 1
    
    print("Accuracy:", '{:.1%}'.format(correct_answer/len(raw_ans)))
    print("Wrong number lines:")
    for num in wrong_arr:
        print(num)

        
    
