# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P2H01AbA5Lp__3OzOInYTm6uuh0gbLvV
"""

import pandas as pd
import numpy as np

df=pd.read_csv("Tweets.csv")
df.head()

import nltk
nltk.download('stopwords')

import string
from nltk.corpus import stopwords

stopset=stopwords.words('english')

def text_process(msg):
    nopunc =[char for char in msg if char not in string.punctuation]
    nopunc=''.join(nopunc)
    return ' '.join([word for word in nopunc.split() if word.lower() not in stopwords.words('english')])

df.head()

df['tokenized_tweet'] = df['text'].apply(text_process)

df['tokenized_tweet']

nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.tokenize import sent_tokenize, word_tokenize
def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(wordnet_lemmatizer.lemmatize(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

df['tokenized_tweet']=df['tokenized_tweet'].apply(stemSentence)

df['tokenized_tweet']

df=df[['tokenized_tweet']]

df.head()