'''
this script will take the existing csv with information from the bills and convert the text into a form useable by our machine learning model

@author: Brian Echavarria (be2298)
'''
import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

og_df = pd.read_csv("csv-files/votes.csv")
og_df = og_df.dropna()
df = og_df.head(1000)

#special splitter function to handle both cases in the Issues column
def splitter(string):
    string = string[:-1]
    string = string[:len(string)//2]
    if ',' in string:
        return string.split(',')
    else:
        return string.split('and')

def punctuation_deleter(sentence):
    sentence = str(sentence)
    for c in sentence:
        if c in string.punctuation:
            sentence = sentence.replace(c, "")
    
    return sentence


def stopword_remover(sentence):
    words = sentence.split(" ")
    for w in words:
        if w in stopwords.words('english'):
            words.remove(w)


    return words

# #TODO:
# def message_transformer(sentence):


#     return 1

df = df.drop('Vote_Title', axis=1)

df["Vote_Issues"] = df["Vote_Issues"].apply(splitter).apply(lambda x: [y.strip().lower() for y in x])

# df["Vote_Summary"] = df["Vote_Summary"].str.lower()
# df["Vote_Summary"] = df["Vote_Summary"].apply(punctuation_deleter).apply(stopword_remover)


mlb = MultiLabelBinarizer(sparse_output=True)

df = df.join(
            pd.DataFrame.sparse.from_spmatrix(
                mlb.fit_transform(df.pop('Vote_Issues')),
                index=df.index,
                columns=mlb.classes_))


X_train, X_test, y_train, y_test = train_test_split(df[numerical_features + [text_feature]], df['label'], test_size=0.2, random_state=42)

text_transformer = TfidfVectorizer(max_features=1000, stop_words='english')
prerocessor = ColumnTransformer(
    transformers = [
        ('text', text_transformer, 'Vote_Summary')
    ]
)

#Used this one time to get the issues that appear in the dataset in order to perform 1 hot encoding

# issues = set()
# for line in og_df.Vote_Issues.unique():
#     temp = splitter(line)
#     for t in temp:
#         issues.add(t.strip())

# print(issues)

print(df)
