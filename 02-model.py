import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn_pandas import DataFrameMapper
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from utils import HexTransformer

import mummify

df = pd.read_csv("data/citrus.csv")
target = "fruit"
y = df[target]
X = df.drop(target, axis=1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

mapper = DataFrameMapper(
    [
        ("hexcode", HexTransformer(), {"input_df": True}),
        (["diameter"], StandardScaler()),
        (["weight"], StandardScaler()),
    ],
    df_out=True,
)

Z_train = mapper.fit_transform(X_train)
Z_test = mapper.transform(X_test)

model = KNeighborsClassifier(n_neighbors=4)
pipe = make_pipeline(mapper, model)
pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)

with open("pipe.pkl", "wb") as f:
    pickle.dump(pipe, f)

mummify.log(f"Accuracy: {round(score, 4)}")
