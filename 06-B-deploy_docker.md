### Deploy: Docker

**Docker Container**

1. Check out the [uwsgi-nginx-flask-docker](https://github.com/tiangolo/uwsgi-nginx-flask-docker) image documentation
2. Make sure your app conforms to the exact `app/` > `main.py` > `app()` structure as specified above
3. Create a `Dockerfile` with:

```
FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install --r requirements.txt
```

4. Test it locally:

```
cd app &&\
export FLASK_APP=main &&\
export FLASK_RUN_PORT=8000 &&\
export FLASK_ENV=development &&\
flask run
```

**Initial Server Setup**

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



build:
	docker build -t appimage .
run:
	docker run -d --name appcontainer -p 80:80 appimage
stop:
	docker stop appcontainer
cleanup:
	docker rmi -f appimage &&\
	docker rm appcontainer