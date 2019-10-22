### Deploy to Heroku Instructions

```
pipenv install scikit-learn pandas dill flask gunicorn
pipenv run python model.py
touch Procfile
echo "web: gunicorn app:app --log-file -" >> Procfile
pipenv run pip freeze > requirements.txt
git init # if not already a git repo
heroku login
heroku git:remote -a repomatic3000
git add .
git commit -m '🚀'
git push heroku master
```

