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

print(houseList)