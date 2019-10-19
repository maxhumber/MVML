import pandas as pd

df = pd.DataFrame([
    ['a', 1],
    ['b', 1],
    ['c', 1],
    ['a', 2],
    ['c', 3],
    ['b', 4],
    ['c', 4]
], columns=['item', 'user'])


from sklearn.feature_extraction.text import CountVectorizer

def squish(df, user='user', item='item'):
    df = df.groupby([user])[item].apply(lambda x: ','.join(x))
    X = pd.DataFrame(df)['item']
    return X

cv = CountVectorizer(tokenizer=lambda x: x.split(','))
X = squish(df)
cv.fit_transform(X).todense()

# matrix([[1, 1, 1],
#         [1, 0, 0],
#         [0, 0, 1],
#         [0, 1, 1]], dtype=int64)

new_user = pd.DataFrame([
    ['c', 5],
    ['d', 5]
], columns=['item', 'user'])

X_new = squish(new_user)
cv.transform(X_new).todense()

# matrix([[0, 0, 1]])
