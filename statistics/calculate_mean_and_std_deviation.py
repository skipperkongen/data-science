# How to calculate mean and standard deviation in pure python and with numpy/pandas
import math
import numpy as np

# Create test data using numpy
mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 100000)
print "Sample of s: ", s[:5]

print 
print "First, in pure python..."
# Calculate mean
mean = s.sum() / len(s)
print mean

# Calculate standard deviation
t = (s - mean) ** 2
print math.sqrt(t.sum() / len(t))

print 
print "Now, with numpy..."
# Of course this can also be done by numpy
print np.mean(s)
print np.std(s)