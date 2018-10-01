# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import warnings

warnings.filterwarnings("ignore")
# Importing the dataset
dataset = pd.read_csv('ISEAR.csv', header=None).iloc[:, :2]


# Cleaning the texts
import re
import nltk
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 7517):
    review = re.sub('[^a-zA-Z]', ' ', dataset.iloc[i, 1])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    review = ' '.join(review)
    corpus.append(review)

# Ignore warning
import warnings
warnings.filterwarnings("ignore")

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=15000)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 0].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# load the model from disk
classifier = pickle.load(open("model.sav", 'rb'))


def predict_tweet(statement):
    inp = statement.lower()
    inp = ps.stem(inp)
    inp = cv.transform([inp]).toarray()
    res = classifier.predict(inp)
    return labelencoder_y.inverse_transform(res)
