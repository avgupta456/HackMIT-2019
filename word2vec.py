from gensim.models import KeyedVectors as kv
import gensim.downloader as api

info = api.info()  # show info about available models/datasets
model = api.load("glove-twitter-25")  # download the model and return as object ready for use

print(model.similarity("apples", "apple"))
