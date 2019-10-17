import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# Quick Data Prep

df = pd.read_csv('data/stars.csv')
df = df.rename(columns={'stargazers': 'stars'})
df = df[df['repo'] != 'maxhumber/gazpacho']
df = df.groupby(['user'])['repo'].apply(lambda x: ','.join(x))
df = pd.DataFrame(df)


cvec = CountVectorizer(tokenizer=lambda x: x.split(','), max_features=1000)
Z_train = cvec.fit_transform(df['repo'])

model = NearestNeighbors(n_neighbors=5, metric='euclidean')
model.fit(Z_train)
distances, indices = model.kneighbors(Z_train)

neighbors = indices[0]
starred = df.iloc[neighbors[0]]['repo'].split(',')

repos = []
for n in neighbors:
    r = df.iloc[n]['repo'].split(',')
    repos.extend(r)

[r for r in repos if r not in starred]
