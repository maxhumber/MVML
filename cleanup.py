from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
from flask import Flask, request, render_template
import dill

app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = dill.load(f)

model.predict(['networkx/networkx,streamlit/streamlit,huggingface/transformers,plasticityai/supersqlite,encode/httpx,aws/chalice,uber/causalml'])

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
