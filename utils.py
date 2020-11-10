import subprocess
import pandas as pd


class HexTransformer:
    @staticmethod
    def hex2rgb(hex):
        hex = hex.replace("#", "")
        return int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.apply(self.hex2rgb).apply(pd.Series)

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)


def clean_up():
    subprocess.run(
        "rm -rf .mummify .venv __pycache__ .ipynb_checkpoints mummify.log Procfile requirements.txt runtime.txt pipe.pkl Dockerfile",
        shell=True,
    )


if __name__ == "__main__":
    clean_up()
