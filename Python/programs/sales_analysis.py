"""
Upload the dataset sales_data.csv to your Google Drive.

Create a new Google Colab file and connect it to your Google Drive.

Display the first 5 rows of the dataset.

Add a text block and create a heading “Data Transformation”. In it, perform the following operations on the columns:

Convert the Order_Date column to the datetime type.

Delete the Time column.

Create a new column sales_amount = Sales * Quantity.

Transform the Gender column so that it contains the values F and M.

Convert the column names to lowercase letters.

💡 It is good practice to check the data after manipulations. Use the head() and info() methods for this purpose.

Add a text block and create a heading “Descriptive Analytics”. In it, perform the following:

What is the maximum and minimum sales amount (sales_amount)? What is the total, average, and median of this metric? Create a text block and write the answers to these questions.
How many product categories does the company sell? What is the popularity of each category? Create text blocks and write the answers to these questions.
Name the top 5 most popular products. Create a text block and write the answer to this question.
Who purchases more often, women or men? Create a text block and write the answer to this question.
What is the most popular payment method? Create a text block and write the answer to this question.
"""

from datetime import date
# Connecting Google Drive
import pandas as pd
from pandas import to_datetime

"""
from google.colab import drive
drive.mount("/content/drive")
# Changing work folder
%cd "/content/drive/My Drive/Data Analyst/Python"
"""

def decode_gender(gender) -> str:
  if gender=="Male":
    return "M"
  elif gender == "Female":
    return "F"
  else:
    return " "


# import CSV file
#mobile_data = pd.read_csv("mobile_sales.csv",nrows=100)
sales_data = pd.read_csv("G:/My Drive/Data Analyst/Python/data/sales_data.csv",nrows=100)
sales_data.head()
sales_data.info()

sales_data["Order_Date"]=to_datetime(sales_data["Order_Date"],format="%Y-%m-%d")
sales_data=sales_data.drop("Time",axis=1)
sales_data["sales_amount"]=sales_data["Sales"] * sales_data["Quantity"]
sales_data["Gender"]=sales_data["Gender"].apply(decode_gender)
sales_data.columns = sales_data.columns.str.lower().str.replace(" ","_")



#Transform the Gender column so that it contains the values F and M.

#Convert the column names to lowercase letters.

sales_data.info()
print(sales_data)


"""
mobile_data.info()
mobile_data["Price Each"] = mobile_data["Price Each"].str.replace(",",".").astype(float)
mobile_data["Order Date"] = pd.to_datetime(mobile_data["Order Date"], format="%m/%d/%y %H:%M")


mobile_data["address"] = mobile_data["Purchase Address"].str.split(",").str[0]
mobile_data["city"] = mobile_data["Purchase Address"].str.split(",").str[1]
mobile_data["zip_code"] = mobile_data["Purchase Address"].str.split(",").str[2]

mobile_data.info()

mobile_data=mobile_data.drop("Purchase Address",axis=1)

mobile_data["sales_amount"]=mobile_data["Price Each"] * mobile_data["Quantity Ordered"]

mobile_data["sales_category"]=mobile_data["sales_amount"].apply(sales_to_category)

mobile_data.head()

mobile_data.columns = mobile_data.columns.str.lower().str.replace(" ","_")
#mobile_data.columns = mobile_data.columns.str.lower().str.replace(" ", "_")

mobile_data.info()

mobiledf = pd.DataFrame(sales_data)
sales_numeric=salesdf[["Sales", "Quantity", "Discount", "Profit", "Shipping_Cost"]]
sales_categorical = salesdf[["Customer_Id", "Gender", "Product_Category", "Product", "Payment_method"]]

print(sales_numeric)
print(sales_categorical.iloc[:100,0])

#print(sales_numeric.iloc[:5,:])


#print(sales_data.index)
#print(sales_data.shape)
#print(sales_data.dtypes)
#sales_data.describe()
"""
