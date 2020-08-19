### Deploy Heroku

1. Setup a virtual environment:

```
python -m venv .venv
```

2. Activate it:

```
source .venv/bin/activate
```

3. Install app and model dependencies (`gunicorn` will always be required):

```
pip install gunicorn flask scikit-learn pandas sklearn_pandas mummify 
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
echo "python-3.8.3" >> runtime.txt
```

7. Create a `Procfile`:

```
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

10. Create a project:

```
heroku create
```

11. Add a remote to the randomly generated project:

```
heroku git:remote -a silly-words-009900
```

12. Test the app locally:

```
heroku local
```

13. (Optional) Deactivate the virtual environment:

```
deactivate
```

14. add, commit push:

```
git add .
git commit -m '🚀'
git push heroku master
```

15. Click on the url and make sure it works!