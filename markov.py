import random
import codecs
import unicodedata

def text_to_array():
    with codecs.open ("test_text.txt", encoding='utf-8') as myfile:
        data=myfile.read().replace('\n', ' ')
        words = data.split()

    return words

def make_lowercase(words):
    lowercase_words = [word.lower() for word in words]
    return lowercase_words

def make_chain(words): 
    chain = {}
    phrase = (words[0], words[1])
    
    for word in words[2:]:
        if phrase in chain:
            chain[phrase].append(word)

        else:
            chain[phrase] = [word]

        phrase = (phrase[1], word)

    return chain

def generate(chain):
    seed = random.choice(chain.keys())
    final_words = []

    for new_words in range(100):

        if seed not in chain:
            break

        picked = random.choice(chain[seed])
        final_words.append(picked)
        seed = (seed[1], picked)

    final = " ".join(final_words)
    return final

def main():
    words = text_to_array()
    lowercase_words = make_lowercase(words)
    chain = make_chain(lowercase_words)
    final = generate(chain)
    return final #unicodedata.normalize('NFKD', u'{}'.format(final.decode('utf-8').encode('utf-8'))).encode('ASCII', 'ignore')
# generate(chain)

#print chain

# chain = main()

print "markov.py successfully ran"

if __name__ == "__main__": main()
