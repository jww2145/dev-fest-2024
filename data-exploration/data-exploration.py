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
    temp = re.split(r'[;,/]', string)
    for i in range(len(temp)):
        if "clean air" in temp[i] and "clean water" in temp[i]:
            temp[i] = "air"
            temp.append("water")
        elif "clean air" in temp[i]:
            temp[i] = "air"
        elif "clean water" in temp[i]:
            temp[i] = "water"
        elif "climate" in temp[i]:
            temp[i] = "climate"
        elif "energy" in temp[i]:
            temp[i] = "energy"
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
        elif "climate" in temp[i]:
            temp[i] = "climate"
        elif "energy" in temp[i]:
            temp[i] = "energy"
    return temp

#preparing the senators data for further working
senatorsDF["Vote_Issues"] = senatorsDF.apply(lambda x: splitter2(x) if x["Vote_Year"] == 2023 else splitter(x), axis=1).apply(lambda x: [y.strip().lower() for y in x])

#analyzing by current senator
bySenator = senatorsDF[senatorsDF['Senator'].isin(senatorsList)].groupby("Senator")

sensDF = pd.DataFrame(columns = ["State", "Party", "Pro-Environment Rating"], index = senatorsList)
pros = bySenator["Vote"].apply(lambda x: (x == "+").sum())
for s, p in pros.items():
    party = senatorsDF[senatorsDF["Senator"]==s]["Party"].iloc[0]
    state = senatorsDF[senatorsDF["Senator"]==s]["State"].iloc[0]
    votes = len(bySenator.get_group(s))
    percent = p/votes
    sensDF.loc[s, ["State", "Party", "Pro-Environment Rating"]] = {"State":state, "Party":party, "Pro-Environment Rating":percent}
    

#analyze by bill
byBill = senatorsDF.groupby("Vote_Title")["Vote"].value_counts()


# for bill_name, bill in byBill:

#     print(1)

#analyze by year
years = senatorsDF.Vote_Year.unique()

issuesDF = senatorsDF.explode("Vote_Issues")

#find all the issues that are discussed
issue_list = list(set(issuesDF["Vote_Issues"].tolist()))
issues_by_year = pd.DataFrame(0.0, index = years, columns = issue_list)

#create a dictionary for the relevance of an issue in a particular year
for y in years:

    info = senatorsDF[senatorsDF["Vote_Year"]==y]
    num_bills = info.shape[0]
    counted_values = Counter(issue for issues in info["Vote_Issues"] for issue in issues)
    for item, amt in counted_values.items():
        issues_by_year.loc[y, item] = amt/num_bills

issues_by_year =  issues_by_year[::-1] #sorting years ascending instead of descending
#used one to create a json for webapp
issues_by_year.to_json('issues.json', orient='index')

#plot the issues relevance over time
for column in issues_by_year.columns:
    plt.plot(issues_by_year.index, issues_by_year[column], label=column)

plt.xlabel("Year")
plt.ylabel("Relevance")
plt.title("Issue Relevance in Senate by Year")
plt.legend()

#display plot
#plt.show()


    
print(sensDF)