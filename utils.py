import subprocess
import pandas as pd

class DateEncoder:
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        month = X.dt.month
        day_of_week = X.dt.dayofweek
        return pd.concat([month, day_of_week], axis=1)
    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)

def clean_up():
    subprocess.run('rm -rf .mummify .venv __pycache__ .ipynb_checkpoints mummify.log Procfile requirements.txt runtime.txt pipe.pkl', shell=True)

if __name__ == '__main__':
    clean_up()
