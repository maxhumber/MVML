import pickle
import random
from flask import Flask, request, render_template
from sklearn.base import TransformerMixin
import pandas as pd

app = Flask(__name__, template_folder="templates")

class DateEncoder(TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        month = X.dt.month
        day_of_week = X.dt.dayofweek
        return pd.concat([month, day_of_week], axis=1)

with open("pipe.pkl", "rb") as f:
    pipe = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def predict():
    form = request.form
    new = pd.DataFrame({
        'date': [pd.Timestamp(form['date'])],
        'origin': [form['origin']],
        'destination': [form['destination']],
        'stops': [form['stops']]
    })
    price = int(round(pipe.predict(new)[0], -1))
    price = "${:,.2f}".format(price)
    return render_template("result.html", price=price)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
