'''
this script will take the existing csv with information from the bills and convert the text into a form useable by our machine learning model

@author: Brian Echavarria (be2298)
'''
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

df = pd.read_csv("bills.csv")

def splitter(string):
    if ',' in string:
        return string.split(',')
    else:
        return string.split('and')

df["Issues"] = df["Issues"].apply(splitter).apply(lambda x: [y.strip().lower() for y in x])

df["Bill"] = df["Bill"].str.lower()

df["Summary"] = df["Summary"].str.lower()

print(df)
