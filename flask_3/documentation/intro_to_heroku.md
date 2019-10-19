# Getting Started on Heroku with Python

[source](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)

The tutorial assumes that you have:

- a free [Heroku account](https://signup.heroku.com/signup/dc).
- Python version 3.7 installed locally - see the installation guides for [OS X](http://docs.python-guide.org/en/latest/starting/install3/osx/), [Windows](http://docs.python-guide.org/en/latest/starting/install3/win/), and [Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/).

## [Set up](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#set-up)

Mac:

```term
brew install heroku/brew/heroku
```

Once installed, you can use the `heroku` command from your command shell.

Use the `heroku login` command to log in to the Heroku CLI:

```term
heroku login
heroku: Press any key to open up the browser to login or q to exit
 ›   Warning: If browser does not open, visit
 ›   https://cli-auth.heroku.com/auth/browser/***
heroku: Waiting for login...
Logging in... done
Logged in as me@example.com
```

This command opens your web browser to the Heroku login page. If your browser is already logged in to Heroku, simply click the **Log in** button displayed on the page.

## [Prepare the app](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#prepare-the-app)

In this step, you will prepare a simple application that can be deployed.

To clone the sample application so that you have a local version of  the code that you can then deploy to Heroku, execute the following  commands in your local command shell or terminal:

```term
git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started
```

You now have a functioning git repository that contains a simple application, a `runtime.txt` specifying Python 3.7.3, and a `requirements.txt`, which is used by Python’s dependency manager, Pip.

## [Deploy the app](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#deploy-the-app)

In this step you will deploy the app to Heroku.

Create an app on Heroku, which prepares Heroku to receive your source code:

```term
heroku create
Creating app... done, ⬢ serene-caverns-82714
https://serene-caverns-82714.herokuapp.com/ | https://git.heroku.com/serene-caverns-82714.git
```

When you create an app, a git remote (called `heroku`) is also created and associated with your local git repository.

Heroku generates a random name (in this case `serene-caverns-82714`) for your app, or you can pass a parameter to specify your own app name.

Now deploy your code:

```term
git push heroku master

Counting objects: 407, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (182/182), done.
Writing objects: 100% (407/407), 68.65 KiB | 68.65 MiB/s, done.
Total 407 (delta 199), reused 407 (delta 199)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote:        Using supported version of Python 3.7 (python-3.7.3)
remote: -----> Installing python-3.7.3
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting django (from -r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/32/ab/22530cc1b2114e6067eece94a333d6c749fa1c56a009f0721e51c181ea53/Django-2.1.2-py3-none-any.whl (7.3MB)
remote:        Collecting gunicorn (from -r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/8c/da/b8dd8deb741bff556db53902d4706774c8e1e67265f69528c14c003644e6/gunicorn-19.9.0-py2.py3-none-any.whl (112kB)
remote:        Collecting django-heroku (from -r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/59/af/5475a876c5addd5a3494db47d9f7be93cc14d3a7603542b194572791b6c6/django_heroku-0.3.1-py2.py3-none-any.whl
remote:        Collecting pytz (from django->-r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB)
remote:        Collecting psycopg2 (from django-heroku->-r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/37/88/40748331bf75d068a07bbea7dc658faceb0ce2e9fffdde550e76d5475e59/psycopg2-2.7.5-cp37-cp37m-manylinux1_x86_64.whl (2.7MB)
remote:        Collecting dj-database-url>=0.5.0 (from django-heroku->-r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/d4/a6/4b8578c1848690d0c307c7c0596af2077536c9ef2a04d42b00fabaa7e49d/dj_database_url-0.5.0-py2.py3-none-any.whl
remote:        Collecting whitenoise (from django-heroku->-r /tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/07/2e/c77e71cb448f1a507bc2dfec1d5c24e35d14a737837bea6cdfd6d1ff66bd/whitenoise-4.1-py2.py3-none-any.whl
remote:        Installing collected packages: pytz, django, gunicorn, psycopg2, dj-database-url, whitenoise, django-heroku
remote:        Successfully installed dj-database-url-0.5.0 django-2.1.2 django-heroku-0.3.1 gunicorn-19.9.0 psycopg2-2.7.5 pytz-2018.5 whitenoise-4.1
remote:
remote: -----> $ python manage.py collectstatic --noinput
remote:        120 static files copied to '/tmp/build_394859b69f6aeb1b63e599ce5b6c69bd/staticfiles', 376 post-processed.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 57.1M
remote: -----> Launching...
remote:        Released v5
remote:        https://serene-caverns-82714.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/serene-caverns-82714.git
 * [new branch]      revert-to-requirements -> master
```

The application is now deployed. Ensure that at least one instance of the app is running:

```term
heroku ps:scale web=1
```

Now visit the app at the URL generated by its app name.  As a handy shortcut, you can open the website as follows:

```term
heroku open
```

## [View logs](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#view-logs)

Heroku treats logs as streams of time-ordered events aggregated from  the output streams of all your app and Heroku components, providing a  single channel for all of the events.

View information about your running app using one of the [logging commands](https://devcenter.heroku.com/articles/logging), `heroku logs --tail`:

```term
heroku logs --tail

2018-10-12T19:13:57.748721+00:00 heroku[web.1]: Starting process with command `gunicorn gettingstarted.wsgi`
2018-10-12T19:13:59.308299+00:00 app[web.1]: [2018-10-12 19:13:59 +0000] [4] [INFO] Starting gunicorn 19.9.0
2018-10-12T19:13:59.308880+00:00 app[web.1]: [2018-10-12 19:13:59 +0000] [4] [INFO] Using worker: sync
2018-10-12T19:13:59.308777+00:00 app[web.1]: [2018-10-12 19:13:59 +0000] [4] [INFO] Listening at: http://0.0.0.0:3142 (4)
2018-10-12T19:13:59.313176+00:00 app[web.1]: [2018-10-12 19:13:59 +0000] [10] [INFO] Booting worker with pid: 10
2018-10-12T19:13:59.331441+00:00 app[web.1]: [2018-10-12 19:13:59 +0000] [11] [INFO] Booting worker with pid: 11
2018-10-12T19:13:59.864677+00:00 heroku[web.1]: State changed from starting to up
2018-10-12T19:14:03.000000+00:00 app[api]: Build succeeded
2018-10-12T19:19:00.370216+00:00 heroku[router]: at=info method=GET path="/" host=serene-caverns-82714.herokuapp.com request_id=308ae087-635f-4cf8-8ae4-7184dfb23012 fwd="204.14.239.106" dyno=web.1 connect=1ms service=21ms status=200 bytes=7616 protocol=https
```

Visit your application in the browser again, and you’ll see another log message generated.

Press `Control+C` to stop streaming the logs.

## [Define a Procfile](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#define-a-procfile)

Use a [Procfile](https://devcenter.heroku.com/articles/procfile),  a text file in the root directory of your application, to explicitly declare what command should be executed to start your app.

The `Procfile` in the example app you deployed looks like this:

```
web: gunicorn gettingstarted.wsgi --log-file -
```

This declares a single process type, `web`, and the command needed to run it.  The name `web` is important here.  It declares that this process type will be attached to the [HTTP routing](https://devcenter.heroku.com/articles/http-routing) stack of Heroku, and receive web traffic when deployed.

Procfiles can contain additional process types.  For example, you  might declare one for a background worker process that processes items  off of a queue.

### [Microsoft Windows](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#microsoft-windows)

The sample app has an additional Procfile for local development on Microsoft Windows, located in the file `Procfile.windows`.  Later tutorial steps will use this instead: it starts a different web server, one that is compatible with Windows.

```
web: python manage.py runserver 0.0.0.0:5000
```

## [Scale the app](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#scale-the-app)

Right now, your app is running on a single web [dyno](https://devcenter.heroku.com/articles/dynos).  Think of a dyno as a lightweight container that runs the command specified in the `Procfile`.

You can check how many dynos are running using the `ps` command:

```term
heroku ps
Free dyno hours quota remaining this month: 999h 6m (99%)
Free dyno usage for this app: 0h 0m (0%)
For more information on dyno sleeping and how to upgrade, see:
https://devcenter.heroku.com/articles/dyno-sleeping

=== web (Free): gunicorn gettingstarted.wsgi (1)
web.1: up 2018/10/12 14:26:45 -0500 (~ 33s ago)
```

By default, your app is deployed on a free dyno. Free dynos will  sleep after a half hour of inactivity (if they don’t receive any  traffic).  This causes a delay of a few seconds for the first request  upon waking. Subsequent requests will perform normally.  Free dynos also  consume from a monthly, account-level quota of [free dyno hours](https://devcenter.heroku.com/articles/free-dyno-hours) - as long as the quota is not exhausted, all free apps can continue to run.

To avoid dyno sleeping, you can upgrade to a hobby or professional dyno type as described in the [Dyno Types](https://devcenter.heroku.com/articles/dyno-types)  article. For example, if you migrate your app to a professional dyno,  you can easily scale it by running a command telling Heroku to execute a  specific number of dynos, each running your web process type.

Scaling an application on Heroku is equivalent to changing the number  of dynos that are running.  Scale the number of web dynos to zero:

```term
heroku ps:scale web=0
```

Access the app again by hitting refresh on the web tab, or `heroku open` to open it in a web tab.  You will get an error message because you no longer have any web dynos available to serve requests.

Scale it up again:

```term
heroku ps:scale web=1
```

For abuse prevention, scaling a non-free application to more than one dyno requires [account verification](https://devcenter.heroku.com/articles/account-verification).

## [Declare app dependencies](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true#declare-app-dependencies)

Heroku recognizes an app as a Python app by looking for key files. Including a `requirements.txt` in the root directory is one way for Heroku to recognize your Python app.

The demo app you deployed already has a `requirements.txt`, and it looks something like this:

```
django
gunicorn
django-heroku
```

The `requirements.txt` file lists the app dependencies  together. When an app is deployed, Heroku reads this file and installs  the appropriate Python dependencies using the `pip install -r` command.

To do this locally, you can run the following command:

```term
pip install psycopg2-binary
pip install -r requirements.txt
```

Installing the dependencies also caused several other dependencies to be installed. You can see them by using pip’s feature `list`:

```term
pip list

Package         Version
--------------- -------
dj-database-url 0.5.0
Django          2.1.2
django-heroku   0.3.1
gunicorn        19.9.0
pip             10.0.1
psycopg2        2.7.5
pytz            2018.5
setuptools      39.0.1
whitenoise      4.1
```