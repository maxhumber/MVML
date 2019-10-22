Follow instructions for:

https://github.com/tiangolo/uwsgi-nginx-flask-docker



#### Initial Server Setup

Configure DigitalOcean Docker Image

```
ssh root@142.93.XXX.104
```

Update everything:

```
sudo apt update
sudo apt -y upgrade
sudo apt install make
sudo apt install unzip
```

Get new monitoring:

```
curl -sSL https://repos.insights.digitalocean.com/install.sh | sudo bash
```

Create a new user:

```
adduser ninja
```

> password

Adjust permissions:

```
usermod -aG sudo ninja
sudo usermod -aG docker ninja
rsync --archive --chown=ninja:ninja ~/.ssh /home/ninja
```

Sign in with the new user:

```
ssh ninja@142.93.XXX.104
```



#### Get the app on the machine

Option A: Copy files (have to be a directory above the ffninja repo/dir):

```console-bash
scp -r ffninja ninja@142.93.XXX.104:ffninja
```

or ~ Option B:

```
wget https://github.com/maxhumber/ffninja/archive/master.zip
unzip master.zip
mv ffninja-master ffninja
rm -f master.zip
```

probably better for CI later...



#### Build and start Docker

```
cd ffninja
make build
make run
```



#### adding custom url

## Registrar: Namecheap

1. Sign in to your Namecheap account, then click **Domain List**in the left-hand column. You will be presented with a dashboard listing all of your domains. Click the **Manage**button of the domain you’d like to update.

![Namecheap domain dashboard entry](https://assets.digitalocean.com/articles/point_to_nameservers/namecheap-domain-list.png)

2. In the **Nameservers**section of the resulting screen, select **Custom DNS**from the dropdown menu and enter the following nameservers:

- ns1.digitalocean.com
- ns2.digitalocean.com
- ns3.digitalocean.com

![Namecheap custom dns nameserver entry](https://assets.digitalocean.com/articles/point_to_nameservers/namecheap-ns-entries.png)

3. Click the green checkmark to apply your changes. Now you are ready to move on to connecting the domain with your Droplet in the DigitalOcean control panel. Check out the Conclusion section at the end of this article to read on what to do next.



#### In Digital Ocean

Create an A and CNAME record:

| Type  | Hostname                  | Value                               | TTL (seconds) |      |
| ----- | ------------------------- | ----------------------------------- | ------------- | ---- |
| CNAME | www.fantasyfootball.ninja | is an alias offantasyfootball.ninja | 43200         | More |
| A     | fantasyfootball.ninja     | directs to142.93.XXX.104            | 3600          | More |



-----

TravisCI

https://github.com/dwyl/learn-travis/blob/master/encrypted-ssh-keys-deployment.md

### Login

```
ssh root@138.68.163.126
```

### 2. Create a `new` SSH Key

Change directory into the `.ssh`directory on the instance:

```
cd ~/.ssh
ssh-keygen -t rsa -b 4096 -C "TravisCIDeployKey"
```

Add to authorized keys

```
cat id_rsa.pub >> authorized_keys
```

In the git repo on your local host (you should be in that directory) add to git ignore

```
echo "deploy_key" >> .gitignore
```

Download the key?

```
scp ninja@142.93.148.104:/home/ninja/.ssh/id_rsa ./deploy_key
```

Test that we can login:

```
ssh -i ./deploy_key ninja@142.93.148.104
```

Grab the TravisCI

```
gem install travis
```

login to Travis CLI (with github creds)

```
travis login --org
```

Add the encrypted deploy key

```
touch .travis.yml && travis encrypt-file ./deploy_key --add
```

Add the other bits to the file

----



CI strategy

Separate out the initial server setup in a bash script



1. sign on to server

2. delete existing repo

2. download and unzip new code
3. stop container
4. delete old container and image
5. build new image
6. start new container

```
# remove old
rm -rf ffninja
# download new
wget https://github.com/maxhumber/ffninja/archive/master.zip
unzip master.zip
mv ffninja-master ffninja
rm -f master.zip
# cd into new
cd ffninja
ls
# stop and clean up docker
make stop
make cleanup
# rebuild and deploy
make build
make run
```



Could I get it to??

1. sign on to server

2. delete existing repo
3. download and unzip new code
4. build new image
5. stop container
6. start new container
7. deleter old container and image



---





#### TODO:

- Google Analytics

- Fix DEF mappings
- Add FLEX
- Add about page (for VORP methodology)
- CI/CD
- Add https://

- In season roster builder $$$
- Schedule the scrapers
- Seperate out the database... postgres?
- Add rollbar for errors
- Build better documentation
