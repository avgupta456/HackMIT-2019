from gensim.models import KeyedVectors
import gensim.downloader as api

from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer

info = api.info()  # show info about available models/datasets
model = api.load("glove-twitter-25")  # download the model and return as object ready for use

porter = PorterStemmer()
lancaster = LancasterStemmer()

def getSim(w1, w2):
    w1 = porter.stem(w1)
    w2 = porter.stem(w2)
    return model.similarity(w1, w2)

print(getSim("olives","olive oil"))
