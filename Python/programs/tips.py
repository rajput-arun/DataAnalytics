import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")
#print(tips)
max_bins=10
plt.hist(tips["tip"], bins=max_bins)
plt.title("Histogram of tips")
plt.xlabel("Frequency")
plt.ylabel("Tips ($)")

xval = plt.gca().get_xlim()
yval = plt.gca().get_ylim()
#print(xval[0], xval[1])
#print(xval[1]/max_bins)

#x_ticks=np.arange(0,round(xval[1],0)+1,2)
x_ticks=np.arange(0,xval[1]+2,2)
#print(x_ticks)
plt.xticks(x_ticks)

y_ticks=np.arange(yval[0],yval[1],10)
plt.yticks(y_ticks)

plt.show()
