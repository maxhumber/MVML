### Deploy to Heroku

1. Setup a virtual environment:

```sh
python -m venv .venv
```

2. Activate it:

```sh
source .venv/bin/activate
```

3. Install app and model dependencies (`gunicorn` will always be required):

```sh
pip install gunicorn flask scikit-learn pandas sklearn_pandas mummify 
```

3. Freeze the dependencies:

```sh
pip freeze > requirements.txt
```

4. Retrain the model inside of the virtual environment:

```sh
python 02-model.py
```

5. Make sure the app still works locally:

```sh
python 05-app.py
```

6. Specify a python runtime (3.8.x not yet available!):

```sh
python --version
echo "python-3.7.6" >> runtime.txt
```

7. Create a `Procfile`:

```sh
echo "web: gunicorn 05-app:app --log-file -" >> Procfile
```

8. If your project isn't already a git repo, make it one:

```sh
git init
```

9. Login to Heroku from the [command line](https://devcenter.heroku.com/articles/heroku-cli):

```sh
heroku login
```

10. Create a project:

```sh
heroku create
```

11. Add a remote to the randomly generated project:

```sh
heroku git:remote -a silly-words-009900
```

12. Test the app locally:

```sh
heroku local
```

13. (Optional) Deactivate the virtual environment:

```sh
deactivate
```

14. add, commit push:

```sh
git add .
git commit -m '🚀'
git push heroku master
```

15. Click on the url and make sure it works!