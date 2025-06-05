import pandas as pd
from spacy.lang.ru.stop_words import STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv(r"app/entites/fakenews_dataset/train.tsv", sep="	")

X = df['title']
y = df['is_fake']

tfidf = TfidfVectorizer(stop_words=list(STOP_WORDS))

X_train = tfidf.fit_transform(X)

nb = MultinomialNB()
nb.fit(X_train, y)

def predict(data):
    data = [data]
    data = tfidf.transform(data)
    return nb.predict(data)