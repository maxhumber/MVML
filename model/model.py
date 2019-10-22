from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import dill

import mummify

df = pd.read_csv("data/stars.csv")
df = df[df["repo"] != "maxhumber/gazpacho"]
df = df[df.language.isin(["Python", "Jupyter Notebook"])]
popular = pd.DataFrame(df["repo"].value_counts())
select_repos = popular[popular["repo"] >= 5].index.tolist()
df = df[df["repo"].isin(select_repos)]
df = df.groupby(["user"])["repo"].apply(lambda x: ",".join(x))
df = pd.DataFrame(df)


class NNRecommender:
    def __init__(
        self, n_neighbors=10, max_features=1000, tokenizer=lambda x: x.split(",")
    ):
        self.cv = CountVectorizer(tokenizer=tokenizer, max_features=max_features)
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)

    def fit(self, X):
        self.X = X
        X = self.cv.fit_transform(X)
        self.nn.fit(X)
        return self

    def predict(self, X):
        Xp = []
        for Xi in X:
            Xt = self.cv.transform([Xi])
            _, neighbors = self.nn.kneighbors(Xt)
            repos = []
            for n in neighbors[0]:
                r = self.X.iloc[int(n)].split(",")
                repos.extend(r)
            repos = list(set(repos))
            repos = [r for r in repos if r not in Xi.split(",")]
            Xp.append(repos)
        return Xp

n_neighbors = 10
max_features = 1000
model = NNRecommender(n_neighbors, max_features)
model.fit(df["repo"])

with open("model/model.pkl", "wb") as f:
    dill.dump(model, f)

mummify.log(f'n_neighbors={n_neighbors}, max_features={max_features}')
