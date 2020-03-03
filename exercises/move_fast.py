# from https://scikit-learn.org/stable/auto_examples/linear_model/plot_ransac.html
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression, RANSACRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import mummify

n_samples = 1000
n_outliers = 50

X, y, coef = make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0
)

np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)

with open('exercises/model.pkl', 'wb') as f:
    pickle.dump(model, f)

mummify.log('') # put something in here
