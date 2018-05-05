# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:30:33 2018

@author: Robert Henderson
"""
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')
strng = open("tapper.txt", "r").read()
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)
word_tokens = word_tokenize(strng)

filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w.lower() not in stop_words:
        if w not in punctuation:
            filtered_sentence.append(w.lower())
 
counts = Counter(filtered_sentence)
print(counts)