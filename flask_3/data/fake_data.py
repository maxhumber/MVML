import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

%matplotlib inline
np.set_printoptions(suppress=True)

def b_age(x, a=-725, h=65, k=1_000_000):
    # cap at 65, $1M
    y = a*(x - h)**2 + k
    return y

x = range(18, 100)
y = [b_age(xi) for xi in x]

plt.plot(x, y);

def b_education(years):
    # years after high school
    return years * 75000

x = range(10)
y = [b_education(xi) for xi in x]

plt.plot(x, y);

def b_male(x):
    return x * 100000

x = [0, 1]
y = [b_male(xi) for xi in x]

plt.bar(x, y);

def wealth(age, education, male):
    w = b_age(age) + b_education(education) + b_male(male)
    w += np.random.normal(0, 25000)
    return w if w >= 0 else 0

def fake(n=1000):
    age = np.random.randint(18, 100, size=n)
    education = np.random.poisson(4, size=n)
    male = np.random.binomial(1, 0.5, size=n)
    df = pd.DataFrame({'age': age, 'education': education, 'male': male})
    df['wealth'] = df.apply(lambda row: wealth(row.age, row.education, row.male), axis=1)
    return df

df = fake()
df['gender'] = df['male'].replace({1: 'male', 0: 'female'})
df = df.drop('male', axis=1)
df['education'] = pd.cut(
    df['education'],
    bins=[0, 2, 4, 6, 8, 100],
    labels=['High School', 'Community College', 'University', 'Masters', 'PhD'])
mask = np.random.choice([True, False], p=[0.9, 0.1], size=df.shape)
df = df.mask(~mask)
df = df[['age', 'education', 'gender', 'wealth']]
df.to_csv('data/wealth.csv', index=False)
