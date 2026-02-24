#numpy.random
import numpy as np

# rand() function - generates positive numbers between 0 and 1

var = np.random.rand(4)
print(var)

var = np.random.rand(4,5)
print(var)

# randn() function - generates numbers from standard normal distribution (can be negative)

var = np.random.randn(4)
print(var)

#randf() function - generates random floating point numbers between 0.0 to 1.0

var = np.random.ranf(4)
print(var)

