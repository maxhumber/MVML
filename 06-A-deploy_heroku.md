## Deploy: Heroku

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

12. Add a remote to the randomly generated project:

```
heroku git:remote -a fast-shore-73006
```

13. Test the app locally:

```
heroku local
```

14. add, commit push:

```
git add .
git commit -m '🚀'
git push heroku master
```

15. Click on the url and make sure it works!