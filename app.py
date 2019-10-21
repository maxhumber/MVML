from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
from flask import Flask, request, render_template
import dill
import random

app = Flask(__name__)

with open('model/model.pkl', 'rb') as f:
    model = dill.load(f)

repos = model.cv.get_feature_names()

@app.route('/')
def index():
    random_repos = ','.join(random.choices(repos, k=5))
    return render_template('index.html', random_repos=random_repos)

@app.route('/result', methods=['POST'])
def predict():
    repos = request.form['repos']
    repos = ','.join([r.strip() for r in repos.split(',')])
    suggestions = model.predict([repos])[0]
    return render_template('result.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
