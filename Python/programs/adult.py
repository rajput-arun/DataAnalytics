"""
Read the dataset from the CSV file and clean the data
- Also, verify the correctness of the data (salary and salary in $K).
Obtain age statistics for each education type. Use groupby and describe for this.
Compare the salaries of married and unmarried men. Who earns more? (> 50K or <= 50K) Married men are those whose marital-status starts with Married. Others are considered unmarried.
Find the maximum number of hours a person works per week. How many people work this many hours per week?
"""

from datetime import date
# Connecting Google Drive
import numpy as np
import pandas as pd

"""
from google.colab import drive
drive.mount("/content/drive")
# Changing work folder
%cd "/content/drive/My Drive/Data Analyst/Python/data"
fpath=""
"""
fpath = "g:/My Drive/Data Analyst/Python/data/"
# import CSV file
ds = pd.read_csv(fpath+"adult.csv")
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

male_count = (ds["sex"]=="Male").sum()
female_count = (ds["sex"]=="Female").sum()
print(male_count)
print(female_count)

#Find the average age of men in the dataset.

avg_male_age= ds.loc[ds["sex"]=="Male", "age"].mean()
avg_female_age= ds.loc[ds["sex"]=="Female", "age"].mean()
print(avg_male_age)
print(avg_female_age)

#Calculate the percentage of people from Poland (native-country).
poland_percent = ((ds["native-country"]=="Poland").sum() / ds.shape[0]) * 100
print(f"{poland_percent}%")

#Check if there are people without higher education (education: Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters, Doctorate) but earning > 50K.

qualified = (~ds["education"].isin(["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"]) & (ds["salary"]==">50K")).sum()
print(qualified)

#Obtain age statistics for each education type. Use groupby and describe for this.

age_stats = ds.groupby("education")["age"].describe()
print(age_stats)

#Compare the salaries of married and unmarried men. Who earns more? (> 50K or <= 50K) Married men are those whose marital-status starts with Married. Others are considered unmarried.

ds["married_status"] = (
    (ds["sex"] == "Male") &
    ds["marital-status"].str.startswith("Married")
)

men = ds[ds["sex"] == "Male"]
#men["married_status"] = men["marital-status"].str.startswith("Married")
#men.loc[:, "married_status"] = men["marital-status"].str.startswith("Married")

salary_comparison = (
    men
    .groupby("married_status")["salary"]
    .value_counts()
    .unstack()
)
percentage = salary_comparison.div(salary_comparison.sum(axis=1), axis=0) * 100

print(percentage)

max_hours = ds["hours-per-week"].max()
count_max_hours = (ds["hours-per-week"] == max_hours).sum()

print("Max hours per week:", max_hours)
print("Number of people working max hours:", count_max_hours)


