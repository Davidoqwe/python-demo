# Mean, median, and mode
# Use the NumPy mean() method to find the average speed:
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)
# meadian
# Use the NumPy median() method to find the middle value:
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
# Using the NumPy module:
import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
# Mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
 
# Machine Learning - Standard Deviation
import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)
# Example
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)
# variance
# use the numpy var() method to find the variance:
import numpy

speed =[32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)
# Standard Deviation
#Use the NumPy std() method to find the standard deviation:
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)
# Machine learning - percentiles
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

# what is the age that 90% of the people are younger than?
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)
#Machine Learning - Data Distribution
#Create an array containing 250 random floats between 0 and 5:
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)
#Histogram
#Draw a histogram

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

#Big Data Distributions
#Create an array with 100000 random numbers, and display them using a histogram with 100 bars:
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()

#Machine Learning - Normal Data Distribution
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()