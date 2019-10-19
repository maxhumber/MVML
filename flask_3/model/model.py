from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from sklearn.pipeline import make_pipeline
from sklearn_pandas import DataFrameMapper, CategoricalImputer
import pandas as pd
import pickle

df = pd.read_csv('data/wealth.csv')
df = df.dropna(subset=['wealth'])

target = 'wealth'
X = df.drop(target, axis=1)
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

mapper = DataFrameMapper([
    (['age'], [SimpleImputer(), PolynomialFeatures(include_bias=False), StandardScaler()]),
    ('education', [CategoricalImputer(), LabelBinarizer()]),
    ('gender', [CategoricalImputer(), LabelEncoder()])
])

model = LinearRegression()

pipe = make_pipeline(mapper, model)
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
pickle.dump(pipe, open('model/pipe.pkl', 'wb'))

# # load from a model
# del pipe
# pipe = pickle.load(open('model/pipe.pkl', 'rb'))
