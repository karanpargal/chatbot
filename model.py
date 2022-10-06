import json
import string
import random 
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer 
import tensorflow as tf 
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, Dropout

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

words = []
classes = []
doc_X = []
doc_y = []

intents = json.loads(open("intents.json").read())

print(intents)

