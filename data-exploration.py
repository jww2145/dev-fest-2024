import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

senatorsDF = pd.read_csv("csv-files/votes.csv")
senatorsDF = senatorsDF.dropna()

senatorsList = senatorsDF.head(100).Senator.values

#special splitter function to handle both cases in the Issues column
#copied from nlp-prep.py
def splitter(string):
    string = string.lower()
    string = string.rstrip(',')
    string = string[:len(string)//2]
    return re.split(r'\s*(?:and\s*)?[,/]\s*', string)

#preparing the senators data for further working
senatorsDF["Vote_Issues"] = senatorsDF["Vote_Issues"].apply(splitter)

#analyzing by current senator
bySenator = senatorsDF[senatorsDF['Senator'].isin(senatorsList)].groupby("Senator")

#analyze by bill
byBill = senatorsDF.groupby("Vote_Title")

print(byBill.first())