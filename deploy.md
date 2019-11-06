## Deploy: Heroku

1. Setup a pipenv environment:

```
pipenv install scikit-learn pandas dill flask gunicorn
pipenv run python model.py
```

2. Create a `Procfile`:

```
touch Procfile
echo "web: gunicorn app:app --log-file -" >> Procfile
```

3. If your project isn't already a git repo, make it one:

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



## Deploy: Docker + DigitalOcean



#### Docker Container Instructions

1. [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker)

#### Initial Server Setup

2. Configure DigitalOcean Docker Image

3. ssh into the machine:

```
ssh root@142.93.XXX.104
```

4. Update everything:

```
sudo apt update # skip
sudo apt -y upgrade # skip
sudo apt install make
sudo apt install unzip
```

5. Get new monitoring:

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash # skip
```

6. Create a new user:

```
adduser mvml
```

> enter password

7. Adjust permissions:

```
usermod -aG sudo mvml
sudo usermod -aG docker mvml
rsync --archive --chown=mvml:mvml ~/.ssh /home/mvml
```

8. Sign in with the new user:

```
ssh mvml@142.93.XXX.104
```

#### Get the app on the machine

9. Run the following commands:

```
wget https://github.com/maxhumber/mvml/archive/master.zip
unzip master.zip
mv MVML-master repomatic
rm -f master.zip
```

#### Build and start Docker

10. Run the following:

```
cd repomatic
make build
make run
```

