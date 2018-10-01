# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(
    n_estimators=1500, n_jobs=-1, random_state=0)
classifier.fit(X_train, y_train)

# Dump model
import pickle
filename = 'model.sav'
pickle.dump(classifier, open(filename, 'wb'))
