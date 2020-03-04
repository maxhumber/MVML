## Deploy: Heroku

1. Setup a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

2. Install required dependencies:

```
pip install gunicorn flask scikit-learn pandas mummify
```

3. Freeze the dependencies:

```
pip freeze > requirements.txt
```

4. Retrain the model inside of the virtual environment:

```
python 02-model.py
```



4. Create a `Procfile`:

```
touch Procfile
echo "web: gunicorn app:app --log-file -" >> Procfile
```

3. (Sometimes) If your project isn't already a git repo, make it one:

```
git init
```

4. Login to Heroku from the [command line](https://devcenter.heroku.com/articles/heroku-cli):

```
heroku login
```

5. Create a project in the Heroku Web Panel
6. Add your repo to the Heroku project:

```
heroku git:remote -a repomatic3000
```

7. add, commit push:

```
git add .
git commit -m '🚀'
git push heroku master
```

8. Visit the website and make sure it works!
