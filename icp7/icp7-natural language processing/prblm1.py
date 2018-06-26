from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

import re, collections
import nltk
from collections import Counter
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk import wordpunct_tokenize, pos_tag, ne_chunk
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
from nltk import trigrams
from nltk.util import ngrams



html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()
soup = BeautifulSoup(html,"lxml")
#[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
[s.extract() for s in soup(['[document]'])]

visible_text = soup.find("p").getText()
print(visible_text)
text_file = open("Output.txt", "w")

text_file.write(visible_text)

text_file.close()

def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())
     
WORDS = tokens(open('output.txt').read())
WORD_COUNTS = collections.Counter(WORDS)
print(WORDS)
#Tokenization
print("----------------------------Tokenization------------")

stokens = nltk.sent_tokenize(visible_text)
wtokens = nltk.word_tokenize(visible_text)
for s in stokens:
#    print("tokens")
    print(s)
for t in wtokens:
#    print("token words")
    print(t)
print(visible_text)
print("-------------------Porter STemming--------------------------")
pStemmer= PorterStemmer()
print(pStemmer.stem(visible_text))
print("-------------------Lancaster STemming--------------------------")
lStemmer= LancasterStemmer()
print(lStemmer.stem(visible_text))
print("-------------------Snowball STemming--------------------------")
sStemmer= SnowballStemmer('english')
print(sStemmer.stem(visible_text))
print("-------------------POS--------------------------")
text = nltk.word_tokenize(visible_text)
print(nltk.pos_tag(text))
print("-------------------Lemmatization--------------------------")

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(visible_text,pos = "a"))
print("----------------Trigram------------------")
text = "Duck, dynamic, strong since version 3.5"
token=nltk.word_tokenize(text)
print(token)
trigrams = ngrams(token,3)
#trigramss=ngrams(visible_text,3)
#trigrams=ngrams(token,3)
#trigramss =  trigrams(visible_text)
print(Counter(trigrams))

Counter({('program', 'in'): 2, ('NLTK', 'that'): 2, ('that', 'breaks'): 2,
 ('write', 'a'): 2, ('breaks', 'a'): 2, ('to', 'write'): 2, ('I', 'need'): 2,
 ('a', 'corpus'): 2, ('need', 'to'): 2, ('a', 'program'): 2, ('in', 'NLTK'): 2,
 ('and', 'fivegrams'): 1, ('corpus', '('): 1, ('txt', 'files'): 1, ('unigrams', 
','): 1, (',', 'trigrams'): 1, ('into', 'unigrams'): 1, ('trigrams', ','): 1,
 (',', 'bigrams'): 1, ('large', 'collection'): 1, ('bigrams', ','): 1, ('of',
 'txt'): 1, (')', 'into'): 1, ('fourgrams', 'and'): 1, ('fivegrams', '.'): 1,
 ('(', 'a'): 1, (',', 'fourgrams'): 1, ('a', 'large'): 1, ('.', 'I'): 1, 
('collection', 'of'): 1, ('files', ')'): 1})
print("--------------Named Entity Recognition------------")
print(ne_chunk(pos_tag(wordpunct_tokenize(visible_text))))
 