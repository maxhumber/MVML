[source](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

# Working with virtual environments

[venv](https://packaging.python.org/key_projects/#venv) allows you to manage separate package installations for different projects. It essentially allows you to create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. It is always recommended to use a virtual environment while developing Python applications.

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace `venv` with `virtualenv` in the below commands.

On macOS and Linux:

```
python -m venv env
```

On Windows:

```
py -m venv env
```

The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it `env`.

venv will create a virtual Python installation in the `env` folder.

You should exclude your virtual environment directory from your version control system using `.gitignore` or similar.

## Activating a virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to *activate* it. Activating a virtual environment will put the virtual environment-specific `python` and `pip` executables into your shell’s `PATH`.

On macOS and Linux:

```
source env/bin/activate
```

On Windows:

```
.\env\Scripts\activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the `env` directory.

On macOS and Linux:

```
which python
.../env/bin/python
```

On Windows:

```
where python
.../env/bin/python.exe
```

As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

## Leaving the virtual environment

If you want to switch projects or otherwise leave your virtual environment, simply run:

```
deactivate
```

If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment. There’s no need to re-create the virtual environment.

## Installing packages

Now that you’re in your virtual environment you can install packages. Let’s install the excellent [Requests](http://docs.python-requests.org/) library from the [Python Package Index (PyPI)](https://packaging.python.org/glossary/#term-python-package-index-pypi):

```
pip install requests
```

pip should download requests and all of its dependencies and install them:

```
Collecting requests
  Using cached requests-2.18.4-py2.py3-none-any.whl
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Using cached chardet-3.0.4-py2.py3-none-any.whl
Collecting urllib3<1.23,>=1.21.1 (from requests)
  Using cached urllib3-1.22-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests)
  Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
Collecting idna<2.7,>=2.5 (from requests)
  Using cached idna-2.6-py2.py3-none-any.whl
Installing collected packages: chardet, urllib3, certifi, idna, requests
Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22
```

## Installing specific versions

pip allows you to specify which version of a package to install using [version specifiers](https://packaging.python.org/glossary/#term-version-specifier). For example, to install a specific version of `requests`:

```
pip install requests==2.18.4
```

To install the latest `2.x` release of requests:

```
pip install requests>=2.0.0,<3.0.0
```

To install pre-release versions of packages, use the `--pre` flag:

```
pip install --pre requests
```

## Upgrading packages

pip can upgrade packages in-place using the `--upgrade` flag. For example, to install the latest version of `requests` and all of its dependencies:

```
pip install --upgrade requests
```

## Using requirements files

Instead of installing packages individually, pip allows you to declare all dependencies in a [Requirements File](https://pip.pypa.io/en/latest/user_guide/#requirements-files). For example you could create a `requirements.txt` file containing:

```
requests==2.18.4
google-auth==1.1.0
```

And tell pip to install all of the packages in this file using the `-r` flag:

```
pip install -r requirements.txt
```

## Freezing dependencies

Pip can export a list of all installed packages and their versions using the `freeze` command:

```
pip freeze
```

Which will output a list of package specifiers such as:

```
cachetools==2.0.1
certifi==2017.7.27.1
chardet==3.0.4
google-auth==1.1.1
idna==2.6
pyasn1==0.3.6
pyasn1-modules==0.1.4
requests==2.18.4
rsa==3.4.2
six==1.11.0
urllib3==1.22
```

This is useful for creating [Requirements Files](https://pip.pypa.io/en/latest/user_guide/#requirements-files) that can re-create the exact versions of all packages installed in an environment.