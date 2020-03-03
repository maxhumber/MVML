import pickle
import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelBinarizer
from sklearn_pandas import DataFrameMapper
from sklearn.linear_model import LinearRegression, Lasso, RANSACRegressor

import mummify

df = pd.read_excel('data/train.xlsx')

df.columns = [c.lower() for c in df.columns]
df['date_of_journey'] = df['date_of_journey'].apply(pd.to_datetime)
df['price'] = df['price'].apply(lambda x: round(x * 0.014))
df['total_stops'] = df['total_stops'].apply(
    lambda x: pd.to_numeric(str(x).split(' ')[0], errors='coerce')
)
df['total_stops'] = df['total_stops'].fillna(0)
df = df.rename(columns={
    'date_of_journey': 'date',
    'total_stops': 'stops',
    'source': 'origin'
})

y = df['price']
X = df[['date', 'origin', 'destination', 'stops']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


class DateEncoder(TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        month = X.dt.month
        day_of_week = X.dt.dayofweek
        return pd.concat([month, day_of_week], axis=1)

mapper = DataFrameMapper([
    ('date', DateEncoder(), {'input_df': True}),
    ('origin', LabelBinarizer()),
    ('destination', LabelBinarizer()),
    ('stops', None)
], df_out=True)

model = LinearRegression()
pipe = make_pipeline(mapper, model)
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)

with open('pipe.pkl', 'wb') as f:
    pickle.dump(pipe, f)

mummify.log(f'R2 Score: {round(score, 4)}')
