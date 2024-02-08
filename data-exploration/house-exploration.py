import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

houseDF = pd.read_csv("csv-files/house_votes.csv")
houseDF = houseDF.dropna()
houseDF["Vote_Year"] = houseDF["Vote_Year"].astype(int)

#creates a list of the current representatives
houseList = houseDF.head(435).Representative.values

#create a list of the years in our data set
years = houseDF.Vote_Year.unique()

#function to split the issues into their individual components
#only works with 2022 data and further in the past
def splitter(row):
    string = row["Vote_Issues"]
    string = string.lower()
    string = string.rstrip(',')
    string = string[:len(string)//2]
    temp = re.split(r'[;,/]', string)
    for i in range(len(temp)):
        if "clean air" in temp[i] and "clean water" in temp[i]:
            temp[i] = "air"
            temp.append("water")
        elif "clean air" in temp[i]:
            temp[i] = "air"
        elif "clean water" in temp[i]:
            temp[i] = "water"
        if "climate" in temp[i]:
            temp[i] = "climate"
        if "energy" in temp[i]:
            temp[i] = "energy"
        if "right to know" in temp[i]:
            temp[i] = "public right to know"
    return temp

#splitter for 2023 senate data
def splitter2(row):
    string = row["Vote_Issues"]
    string = string.lower()
    string = string.rstrip(',')
    temp = re.split(r'[;,/]', string)
    for i in range(len(temp)):
        if "clean air" in temp[i] and "clean water" in temp[i]:
            temp[i] = "air"
            temp.append("water")
        elif "clean air" in temp[i]:
            temp[i] = "air"
        elif "clean water" in temp[i]:
            temp[i] = "water"
        if "climate" in temp[i]:
            temp[i] = "climate"
        if "energy" in temp[i]:
            temp[i] = "energy"
        if "right to know" in temp[i]:
            temp[i] = "public right to know"
    return temp

houseDF["Vote_Issues"] = houseDF.apply(lambda x: splitter2(x) if x["Vote_Year"] == 2023 else splitter(x), axis=1).apply(lambda x: [y.strip().lower() for y in x])
issuesDF = houseDF.explode("Vote_Issues")

#find all the issues that are discussed
issue_list = list(set(issuesDF["Vote_Issues"].tolist()))
issues_by_year = pd.DataFrame(0.0, index = years, columns = issue_list)

#create a dictionary for the relevance of an issue in a particular year
for y in years:

    info = houseDF[houseDF["Vote_Year"]==y]
    num_bills = info.shape[0]
    counted_values = Counter(issue for issues in info["Vote_Issues"] for issue in issues)
    for item, amt in counted_values.items():
        issues_by_year.loc[y, item] = amt/num_bills

issues_by_year =  issues_by_year[::-1] #sorting years ascending instead of descending

#used once to create a csv for webapp
issues_by_year.to_csv('issues.csv', index_label="time")

