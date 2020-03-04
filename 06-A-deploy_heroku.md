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

6. Specify a python runtime:

```
python --version 
echo "python-3.7.4" >> runtime.txt
```

7. Deactivate the virtual environment:

```
deactivate
```

8. Create a `Procfile`:

```
echo "web: gunicorn 05-app:app --log-file -" >> Procfile
```

9. If your project isn't already a git repo, make it one:

```
git init
```

10. Login to Heroku from the [command line](https://devcenter.heroku.com/articles/heroku-cli):

```
heroku login
```

11. Create a project:

```
heroku create
```

12. Test it locally

```
heroku local
```

12. Add your repo to the randomly generated project:

```
heroku git:remote -a young-sea-43650
```

13. add, commit push:

```
git add .
git commit -m '🚀'
git push heroku master
```

14. Visit the website and make sure it works!