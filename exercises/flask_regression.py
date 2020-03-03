import pickle
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

with open('exercises/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route("/")
def index():
    pass

@app.route("/result", methods=["POST"])
def predict():
    new = pd.DataFrame({'X': [20]})
    y = float(model.predict(new)[0])
    return pass
