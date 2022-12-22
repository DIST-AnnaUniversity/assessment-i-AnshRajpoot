import pandas as pd

#read csv file
from google.colab import files
import io
uploaded = files.upload()
df1 = pd.read_csv((uploaded['iris.csv']))
df1
#find the average of petal width
pw_avg=pw_mean/pw_len;
#round off to 2 decimal places
print(round(pw_avg,2))
#print only average
print(pw_avg)
