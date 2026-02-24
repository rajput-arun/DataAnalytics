# Connecting Google Drive
import pandas as pd

"""
from google.colab import drive
drive.mount("/content/drive")
# Changing work folder
%cd "/content/drive/My Drive/Data Analyst/Python"
"""

# import CSV file
netflix_data = pd.read_csv(r"G:\My Drive\Data Analyst\Python\Netflix_titles.csv")
netflix_data.head()

print(netflix_data)

# import XLSX file
netflix_data_xlsx = pd.read_excel(r"G:\My Drive\Data Analyst\Python\Netflix_titles.xlsx")
netflix_data_xlsx.head()
print(netflix_data_xlsx)


# import JSON file
usd_data = pd.read_json("https://api.exchangerate-api.com/v4/latest/USD")
usd_data.head()

print(usd_data)
