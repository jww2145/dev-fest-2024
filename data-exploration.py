import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

senatorsDF = pd.read_csv("csv-files/senate_votes.csv")
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


# for bill_name, bill in byBill:

#     print(1)

#analyze by year
years = senatorsDF.Vote_Year.unique()

year_info = dict()
for y in years:
    info = senatorsDF[senatorsDF["Vote_Year"]==y]
    counted_values = Counter(issue for issues in info["Vote_Issues"] for issue in issues)
    max_value, max_count = max(counted_values.items(), key=lambda x: x[1])

    year_info[y] = (max_value, max_count)
    

