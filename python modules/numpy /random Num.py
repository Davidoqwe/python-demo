


# RANDOM NUMBERS IN NUMPY
# Generate a random integer from 0 to 100:
from numpy import random
x=random.randint(100)
print(x)

from numpy import random
x=random.rand()
print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100        
from numpy import random
x=random.randint(100, size=5)
print(x)
# Generate a 2-D array with 3 rows, each row containing 5 random integers from o to 100
from numpy import random
x=random.randint(100, size=(3, 5))
print(x)

# Generate a 1-D array containing 5 random floats:
from numpy import random
x=random.rand(5)
print(x)

# RANDOM DATA DISTRIBUTION

from numpy import random
x=random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
# Random shuffle elements of following array:
from numpy import random
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
# Generating permutation of arrays
from numpy import random
import numpy as np
arr=np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

# SEABORN MODULE

import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()
# Generate a random normal distribution of size 2*3
from numpy import random 
x=random.normal(size=(2, 3))
print(x)
#Generate a random normal distribution of size 2*3 with mean at 1 and standard deviation of 2:
from numpy import random
x=random.normal(loc=1, scale=2, size=(2, 3))
print(x)


from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.normal(size=1000), kind="kde")
plt.show()

# BINOMIAL DISTRIBUTION

from numpy import random
x=random.binomial(n=10, p=0.5, size=10)
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.binomial(n=10, p=0.5, size=1000))
plt.show


from numpy import random 
import matplotlib.pyplot as plt
import seaborn as sns
data={
    "normal":random.normal(loc=50, scale=5, size=1000),
    "binomial":random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

