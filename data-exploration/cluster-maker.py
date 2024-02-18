import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from senators import senators
from sklearn.preprocessing import StandardScaler
import json


def kmeans_senate_votes(csv_file):

    # Load CSV
    df = pd.read_csv(csv_file,encoding = "ISO-8859-1") 

    # Filter senators
    df = df[df['Senator'].isin(senators.keys())]

    # Select columns
    df = df[['Senator', 'Vote']]
    df = df.dropna()

    # Encode senator name  
    le = LabelEncoder()
    df['Senator'] = le.fit_transform(df['Senator'])

    # Filter out '?' votes
    df = df[df['Vote'] != '?']

    senator_ids = df['Senator'].unique()

    senator_votes = df.groupby('Senator').agg({'Vote': lambda x: (x=='+').sum()/len(x)})
    
    kmeans = KMeans(n_clusters=4).fit(senator_votes)
    
    clusters = []
    for senator_id in senator_ids:
        name = le.inverse_transform([senator_id])[0] 
        cluster = kmeans.labels_[senator_id]
        percentage = senator_votes.loc[senator_id, 'Vote']
        clusters.append((name, str(cluster), round(percentage, 2)))

    return clusters 




json_data = kmeans_senate_votes('/Users/joshiebestie/Coding Projects/dev-fest-2024/csv-library/senate_votes copie.csv')

print(kmeans_senate_votes('/Users/joshiebestie/Coding Projects/dev-fest-2024/csv-library/senate_votes copie.csv'))


with open('clusters.json', 'w') as f:
  json.dump(json_data, f)
