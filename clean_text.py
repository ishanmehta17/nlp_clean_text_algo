import nltk
from nltk.stem import PorterStemmer
import re
import spacy
from string import punctuation

#punctuations
punctuations = []
for p in punctuation:
    #Keeping ' since it could be part of a modal verb like can't, won't etc.
    if p != "'":
        punctuations.append(p)

#stopwords
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
             "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
             'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what',
             'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those','be', 'been', 'being', 'a', 'an', 'the',
             'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
             'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
             'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
             'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'now', '#']

#corpuse of words vocab_1 and vocab_2
vocab_1 = nltk.corpus.words.words()

nlp = spacy.load("en_core_web_sm")
vocab_2 = set(nlp.vocab.strings)

#modal_verbs
modal_verbs = ["can", "can't", "could", "couldn't", "did", "didn't", "may", "might",
    "must", "mustn't", "shall", "shan't", "should", "shouldn't", "will", "won't", "would", "wouldn't"]

#words not in the vocab which are valid
valid_words = ["netflix"]

#stemmer
stemmer = PorterStemmer()

def clean_text(text):
    text = "".join([char for char in text if char not in punctuations])

    tokens = re.split('\s+', text)
    tokens = [t.lower() for t in tokens]
    tokens = [t for t in tokens if t not in stopwords]

    tokens = [stemmer.stem(word) for word in tokens
              if word in vocab_1 or word in vocab_2 or
                 word in valid_words or
                 word in modal_verbs or
                 stemmer.stem(word) in vocab_1 or
                 stemmer.stem(word) in vocab_2]

    return tokens

print(clean_text("Before I cancel this Netflix subscription, any good shows to watch?"))
print(clean_text("So if i renew my 1 month netflix subscription now i will easily be able to watch Elite s5 before it expires"))
