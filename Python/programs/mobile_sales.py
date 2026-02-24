from datetime import date
# Connecting Google Drive
import pandas as pd

"""
from google.colab import drive
drive.mount("/content/drive")
# Changing work folder
%cd "/content/drive/My Drive/Data Analyst/Python"
"""

def sales_to_category(sales_amount: float) -> str:
  if sales_amount < 100:
    return "low"
  elif sales_amount <= 500:
    return "medium"
  else:
    return "high"


# import CSV file
#mobile_data = pd.read_csv("mobile_sales.csv",nrows=100)
mobile_data = pd.read_csv("G:/My Drive/Data Analyst/Python/mobile_sales.csv",nrows=100)
mobile_data.head()

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





"""
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
