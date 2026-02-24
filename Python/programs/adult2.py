"""
Read the dataset from the CSV file and clean the data — remove all rows containing the "?" character in any column.
Calculate the mean and standard deviation of the age for people earning > 50K per year. Then, calculate the same for those earning <= 50K.
Analyze the correlation between the data.
"""

import pandas as pd
import numpy as np

fpath = "g:/My Drive/Data Analyst/Python/data/"
# import CSV file
ds = pd.read_csv(fpath+"adult2.csv")
#ds = pd.read_csv(fpath+"adult.csv",nrows=100)
ds.head()
print(ds)

#remove all rows containing the "?" character in any column.

ds.replace("?",pd.NA,inplace=True)
print(ds)
print(ds.isna().sum())
ds = ds.dropna()
print(ds)

#Display the number of men and women in the dataset.

#Calculate the mean and standard deviation of the age for people earning > 50K per year. Then, calculate the same for those earning <= 50K.
#Using Pivot

earnings_pivot = ds.pivot_table(values="age", index="salary", aggfunc=["count","min","max","mean","std"])
print(earnings_pivot)

