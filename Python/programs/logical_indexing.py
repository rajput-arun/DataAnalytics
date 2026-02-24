"""
Display all elements of the array where the number of clicks is greater than 8,000.
Display the count of such values.
Calculate the percentage of values and display the results on the screen:
more than 4,000 clicks;
no more than 1,000 clicks;
between 5,000 and 7,500 clicks.
"""


import numpy as np
clicks = np.array(np.random.randint(100,10001, size=60, dtype=np.uint16))
#print(clicks)

tot_clk = clicks.size
print(tot_clk)

clk_8k = clicks > 8000
clk_1k = clicks <= 1000
clk_5_7k = (clicks > 5000) & (clicks < 7500)

clk_8k_pct=(clicks[clk_8k].size/tot_clk)*100
print(f"percent:{(clk_8k_pct)}%")
print(f"count of clicks > 8000: {clicks[clk_8k].size}")
print(f"count of clicks < 1000: {clicks[clk_1k].size}")
print(f"count of clicks > 5000 & <7500 : {clicks[clk_5_7k].size}")
