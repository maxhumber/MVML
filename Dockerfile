FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app
RUN pip install scikit-learn pandas dill flask gunicorn
