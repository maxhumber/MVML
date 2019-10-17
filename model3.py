import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import csr_matrix
import warnings
from sklearn.metrics.pairwise import euclidean_distances
from lightfm import LightFM
from lightfm.evaluation import precision_at_k
from lightfm.evaluation import auc_score

warnings.filterwarnings("ignore", category=UserWarning)

# Quick Data Prep

df = pd.read_csv('data/stars.csv')
df = df.rename(columns={'stargazers': 'stars'})
df = df[df['repo'] != 'maxhumber/gazpacho']

# users = df.user.unique()
# i = int(users.shape[0] * 0.80 // 1)
# train = df[df['user'].isin(users[:i])]
# test = df[df['user'].isin(users[i:])]

class Encoder:

    def __init__(self):
        self.items = None

    def transform(self, lst):
        """Returns a dictionary where the keys are the users_ids and the values are the encoded items"""
        if self.items is None:
            self.items = self.__items(lst)

        users = {}
        for item, user in lst:
            users.setdefault(user, set()).add(item)

        return {user: np.array([item in basket for item in self.items], dtype=np.uint8) for user, basket in users.items()}

    def reset(self):
        self.items = None

    @staticmethod
    def __items(lst):
        seen = set()
        items = []
        for item, _ in lst:
            if item not in seen:
                items.append(item)
                seen.add(item)
        return items


df = pd.DataFrame([
    ['marc'],
    ['gazpacho, marc'],
    ['gazpacho, chart'],
    ['chart, mummify']
])

df = pd.DataFrame([
    ['a', 1],
    ['b', 1],
    ['c', 1],
    ['a', 2],
    ['c', 3],
    ['b', 4],
    ['c', 4]
], columns=['item', 'user'])
df

pd.DataFrame([
    [1, 1, 1],
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 1]
], columns=['a', 'b', 'c'])

new_user = [['c', 5], ['d', 5]]

[0, 0, 1]


df = pd.DataFrame([
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1]
], columns = ['gazpacho', 'mummify', 'marc', 'chart', 'sausage link'])

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
model.fit(df)
distances, indices = model.kneighbors(df)
distances, indices

new = [0, 0, 0, 1, 1]
_, indices = model.kneighbors([new])
indices






from sklearn.feature_extraction.text import CountVectorizer

train.repo.unique().shape

cvec = CountVectorizer()

encoder = LabelBinzarizer()
X_train = encoder.fit_transform(train['repo'])
X_train.shape

train['rating'] = 1

df = train.pivot(
    index='user',
    columns='repo',
    values='rating'
).fillna(0)

# The Magic

class InteractionMachine:

    def __init__(self, df, ratings, users, items):
        self._ratings = np.array(df[ratings])
        self._users = np.array(df[users])
        self._items = np.array(df[items])
        # heavy lifting encoders
        self.user_encoder = LabelEncoder()
        self.item_encoder = LabelEncoder()
        # preparation for the csr matrix
        u = self.user_encoder.fit_transform(self._users)
        i = self.item_encoder.fit_transform(self._items)
        lu = len(np.unique(u))
        li = len(np.unique(i))
        # the good stuff
        self.interactions = csr_matrix((self._ratings, (u, i)), shape=(lu, li))

    def get_users(self, encoded=False):
        users = np.unique(self._users)
        if encoded:
            users = self.user_encoder.transform(users)
        return users

    def get_items(self, encoded=False):
        items = np.unique(self._items)
        if encoded:
            items = self.item_encoder.transform(items)
        return items

im = InteractionMachine(df, 'stargazers', 'user', 'repo')


df2 = pd.DataFrame(
    im.interactions.todense(),
    index = im.get_users(),
    columns = im.get_items()
)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)

model.predict



model = LightFM(learning_rate=0.05, loss='warp')

model.fit(im.interactions, epochs=30)

person = 'garrrychan'
person = 'mackenzie-gray'
user_id = im.user_encoder.transform([person])[0]
preds = model.predict(user_id, im.get_items(encoded=True))

pred_df = pd.DataFrame({
    'product': im.get_items(),
    'rating': preds
}).sort_values('rating', ascending=False)
pred_df

precision_at_k(model, im.interactions, k=10).mean()
auc_score(model, im.interactions).mean()

pred_df

reco = pred_df['product'].values.tolist()

tried = df[df['user'] == person]['product'].tolist()

[candy for candy in reco if candy not in tried][:5]


person = 'kitkatkittikat'
df[df['user'] == person]
