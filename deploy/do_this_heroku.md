Deploy to Heroku Instructions

```
python -m venv env
source env/bin/activate
pip install pandas numpy flask matplotlib scikit-learn sklearn-pandas gunicorn
touch Procfile
echo "web: gunicorn app:app --log-file -" >> Procfile
pip freeze > requirements.txt
heroku login
git init
heroku git:remote -a wealth-1
git add .
git commit -m '🚀'
git push heroku master
```

