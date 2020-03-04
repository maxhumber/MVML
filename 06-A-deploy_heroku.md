## Deploy: Heroku

1. Setup a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

2. Install required dependencies:

```
pip install gunicorn flask scikit-learn pandas xlrd sklearn_pandas mummify 
```

3. Freeze the dependencies:

```
pip freeze > requirements.txt
```

4. Retrain the model inside of the virtual environment:

```
python 02-model.py
```

5. Make sure the app still works locally:

```
python 05-app.py
```

6. Deactivate the virtual environment:

```
deactivate
```

7. Create a `Procfile`:

```
touch Procfile
echo "web: gunicorn 05-app:app --log-file -" >> Procfile
```

8. If your project isn't already a git repo, make it one:

```
git init
```

9. Login to Heroku from the [command line](https://devcenter.heroku.com/articles/heroku-cli):

```
heroku login
```

10. Create a project in the Heroku Web Panel

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
