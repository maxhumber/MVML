import pickle
from flask import Flask, request, render_template
import pandas as pd
from utils import DateEncoder

app = Flask(__name__, template_folder="templates")

@app.before_first_request
def load_model():
    global pipe
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
    app.run(host='0.0.0.0', port=80)
