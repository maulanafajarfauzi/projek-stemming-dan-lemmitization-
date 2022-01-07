import nltk
from nltk.stem import PorterStemmer

porter = PorterStemmer()

tokens = ['study','studying','studies','studied']

for token in tokens:
    print(token + " : " + porter.stem(token))
study : studi
studying : studi
studies : studi
studied : studi
from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language='english')

for token in tokens:
    print(token + " : " + snowball.stem(token))
study : studi
studying : studi
studies : studi
studied : studi
from nltk.stem import LancasterStemmer

lancaster = LancasterStemmer()

for token in tokens:
    print(token + " : " + lancaster.stem(token))
study : study
studying : study
studies : study
studied : study
nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /Users/bsi-00/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
True
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for token in tokens:
    print(token + " :  " + lemmatizer.lemmatize(token))
study :  study
studying :  studying
studies :  study
studied :  studied

from nltk.stem import PorterStemmer

porter = PorterStemmer()

tokens = ['player','players','plays','playing','played']

for token in tokens:
    print(token + " : " + porter.stem(token))
player : player
players : player
plays : play
playing : play
played : play
from nltk.stem.snowball import SnowballStemmer

snowball = SnowballStemmer(language='english')

for token in tokens:
    print(token + " : " + snowball.stem(token))
player : player
players : player
plays : play
playing : play
played : play
from nltk.stem.lancaster import LancasterStemmer

lancaster = LancasterStemmer()

for token in tokens:
    print(token + " : " + lancaster.stem(token))
player : play
players : play
plays : play
playing : play
played : play
nltk.download('wordnet')
[nltk_data] Downloading package wordnet to /Users/bsi-00/nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
True
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

for token in tokens:
    print(token + " : " + lemmatizer.lemmatize(token))
player : player
players : player
plays : play
playing : playing
played : played
