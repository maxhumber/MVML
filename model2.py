import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.base import BaseEstimator
from sklearn.pipeline import make_pipeline

# DATA

df = pd.read_csv('data/stars.csv')
df = df[df['repo'] != 'maxhumber/gazpacho']
popular = pd.DataFrame(df['repo'].value_counts())
select_repos = popular[popular['repo'] >= 3].index.tolist()
df = df[df['repo'].isin(select_repos)]
df = df.groupby(['user'])['repo'].apply(lambda x: ','.join(x))
df = pd.DataFrame(df)

# MODEL

cvec = CountVectorizer(tokenizer=lambda x: x.split(','), max_features=1000)
model = NearestNeighbors(n_neighbors=5, metric='euclidean')
X = cvec.fit_transform(df['repo'])
model.fit(X)
distances, indices = model.kneighbors(X)



# PREDICT

user = 'garrrychan'
i = list(df.index).index(user)

neighbors = indices[i]
starred = df.iloc[neighbors[0]]['repo'].split(',')

repos = []
for n in neighbors:
    r = df.iloc[n]['repo'].split(',')
    repos.extend(r)

rec = [r for r in repos if r not in starred]

popular[popular.index.isin(rec)]

# new user

df.iloc[100:101].to_dict(orient='list')

new = pd.DataFrame({
    'repo': ['networkx/networkx,streamlit/streamlit,huggingface/transformers,plasticityai/supersqlite,encode/httpx,aws/chalice,uber/causalml']
})

X_new = cvec.transform(new)
distances, indices = model.kneighbors(X_new)
neighbors = indices[0]

def recommend(neighbors):
    starred = df.iloc[neighbors[0]]['repo'].split(',')
    repos = []
    for n in neighbors:
        r = df.iloc[n]['repo'].split(',')
        repos.extend(r)
    rec = [r for r in repos if r not in starred]
    return popular[popular.index.isin(rec)]

recommend(neighbors)


#
