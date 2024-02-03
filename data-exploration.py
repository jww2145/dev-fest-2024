import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

senatorsDF = pd.read_csv("csv-files/senate_votes copie.csv")
senatorsDF = senatorsDF.dropna()
senatorsDF["Vote_Year"] = senatorsDF["Vote_Year"].astype(int)

senatorsList = senatorsDF.head(100).Senator.values

#special splitter function to handle both cases in the Issues column
#copied from nlp-prep.py
#only works with 2022 data and further in the past
def splitter(row):
    string = row["Vote_Issues"]
    string = string.lower()
    string = string.rstrip(',')
    string = string[:len(string)//2]
    return re.split(r'\s*(?:and\s*)?[,/]\s*', string)

#splitter for 2023 senate data
def splitter2(row):
    string = row["Vote_Issues"]
    string = string.lower()
    string = string.rstrip(',')
    return string.split(";")

#preparing the senators data for further working
senatorsDF["Vote_Issues"] = senatorsDF.apply(lambda x: splitter2(x) if x["Vote_Year"] == 2023 else splitter(x), axis=1)

#analyzing by current senator
bySenator = senatorsDF[senatorsDF['Senator'].isin(senatorsList)].groupby("Senator")

#analyze by bill
byBill = senatorsDF.groupby("Vote_Title")["Vote"].value_counts()


print(senatorsDF)