import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)
pipe = pickle.load(open('model/pipe.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        result = request.form
    age = int(result['age'])
    new = pd.DataFrame({
        'age': [age],
        'education': [result['education']],
        'gender': [result['gender']]
    })
    prediction = pipe.predict(new)[0]
    prediction = '${:,.2f}'.format(prediction)
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run()
