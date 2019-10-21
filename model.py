import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv('data/stars.csv')
df = df[df['repo'] != 'maxhumber/gazpacho']
popular = pd.DataFrame(df['repo'].value_counts())
select_repos = popular[popular['repo'] >= 3].index.tolist()
df = df[df['repo'].isin(select_repos)]
df = df.groupby(['user'])['repo'].apply(lambda x: ','.join(x))
df = pd.DataFrame(df)


class NNRecommender:

    def __init__(self, n_neighbors=10, max_features=1000, tokenizer=lambda x: x.split(',')):
        self.cv = CountVectorizer(tokenizer=tokenizer, max_features=max_features)
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)

    def fit(self, X):
        self.X = X
        X = self.cv.fit_transform(X)
        self.nn.fit(X)
        return self

    def predict(self, X):
        Xt = self.cv.transform(X)
        _, neighbors = self.nn.kneighbors(Xt)
        points = []
        for n in neighbors:
            repos = []
            for ni in n:
                r = self.X.iloc[int(ni)].split(',')
                repos.extend(r)
            repos = list(set(repos))
            points.append(repos)
        return points

model = NNRecommender()
model.fit(df['repo'])
model.predict(df['repo'])[14]
