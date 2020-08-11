import pickle
from flask import Flask, request, render_template
import pandas as pd
from utils import HexTransformer

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
    print(form)
    new = pd.DataFrame(
        {
            "diameter": [float(form["diameter"])],
            "weight": [float(form["weight"])],
            "hexcode": [form["color"]],
        }
    )
    fruit = pipe.predict(new)[0]
    orange = fruit == 'orange'
    return render_template("result.html", orange=orange)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
