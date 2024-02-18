import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from senators import senators

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

    # Encode votes
    df = df.replace(['+'], [1])
    df = df.replace(['-'], [-1]) 

    senator_votes = df.groupby('Senator').agg({'Vote': lambda x: (x=='+').sum()/len(x)})

    # Cluster
    kmeans = KMeans(n_clusters=4).fit(senator_votes)
    labels = kmeans.labels_

    return labels
