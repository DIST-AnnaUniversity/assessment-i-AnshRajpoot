#In this program, you will fit a straight line between petal length and petal width. Suppose the equation is y = ax+b, find the variables a and b first. Then for a new petal width value of 5.1, find the predicted value of y.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#read csv file
from google.colab import files
import io
uploaded = files.upload()
df1 = pd.read_csv((uploaded['iris.csv']))
df1

pw_mean = df1['pw'].mean()
def linear_model(df):
  df['plpw'] = df['pl']*df['pw']
  df['pl^2'] = df['pl']*df['pl']
  sum_pl = df['pl'].sum()
  sum_pw = df['pw'].sum()
  sum_plpw = df['plpw'].sum()
  sum_pl_2 = df['pl^2'].sum()
  n = len(df["pl"])
  num = n*sum_plpw - sum_pl*sum_pw
  denom = n*sum_pl_2 - sum_pl**2
  a = round(num / denom,4)
  pl_mean = df['pl'].mean()
  pw_mean = df['pw'].mean()
  b = round(pw_mean - a * pl_mean,4)
  return b,a

#Take X as petal length
pl_mean = df1['pl'].mean()
pl_mean
#Take y as petal width
pw_mean = df1['pw'].mean()
pw_mean
#Split train and test with 30% and set random state as 0

#use regression from scikit learn

#find b and round off to 2 decimal places
b
print(round(b,2))
#find a and round off to 2 decimal places
a
print(round(a,2))
new_pl = 5.3#new x value
#calculate y 
new_pl=5.3
new_pw = a*new_pl+b
new_pw
print(round(new_pw,2))#round off to 2 decimal places







