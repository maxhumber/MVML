from sklearn.linear_model import LinearRegression, RANSACRegressor
import dill

from flask import Flask, request, render_template

app = Flask(__name__)

with open('exercises/regression.pkl', 'wb') as f:
    dill.dump(model, f)

@app.route("/")
def index():
    pass

@app.route("/result", methods=["POST"])
def predict():
    return pass
