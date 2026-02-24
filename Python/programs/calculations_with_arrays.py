"""
Create a new file and name it Calculations with arrays. Grant edit access to the file.

Perform the following operations on the array of advertisement banner clicks from previous tasks:

Find the average and median number of clicks on the advertisement banner.
Calculate the total number of clicks for the first 30 days and the last 30 days.
Determine which month was more successful.
Find the maximum and minimum number of clicks.
Calculate the range of the dataset — the difference between the maximum and minimum values.
Assume that the cost per advertisement click is $0.03. Calculate the cost of the advertisement for each day as well
as the total advertisement cost.

Add a link to the file in the field on the right.
"""

import numpy as np
clicks = np.array(np.random.randint(100,10001, size=60, dtype=np.uint16))

avg_clicks = np.mean(clicks)
med_clicks = np.median(clicks)
max_clicks = np.max(clicks)
min_clicks = np.min(clicks)
rng_clicks = max_clicks - min_clicks
cost_clicks = clicks * 0.03
tot_cost_clicks = np.sum(cost_clicks)

#click_array=np.reshape(30,2)

click_array=np.reshape(clicks,(30,2))

monthly_clicks=np.sum(click_array,axis=0)
mth1=monthly_clicks[0]
mth2=monthly_clicks[1]

#Find the average and median number of clicks on the advertisement banner.
print(f"Average number of clicks: {avg_clicks}")
print(f"Median number of clicks: {med_clicks}")

#Calculate the total number of clicks for the first 30 days and the last 30 days.
print(f"Clicks on first 30 days of Month :{mth1}")
print(f"Clicks on last 30 days of Month :{mth2}")

#Determine which month was more successful.
print("Month 1 is more successful than Month 2" if mth1>mth2 else "Month 2 is more successful than Month 1")

#Find the maximum and minimum number of clicks.
print(f"Maximum Clicks: {max_clicks}")
print(f"Minimum Clicks: {min_clicks}")

#Calculate the range of the dataset — the difference between the maximum and minimum values.
print(f"Range of clicks: {min_clicks} - {max_clicks}")

#Assume that the cost per advertisement click is $0.03. Calculate the cost of the advertisement for each day as well as the total advertisement cost.
print(f"Cost of advertisement clicks: {cost_clicks}")
print(f"Total cost of advertisement : {tot_cost_clicks}")

