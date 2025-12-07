# MATPLOTLIB PYPLOT
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import numpy as np

xpoints =np.array([0, 6])
ypoints =np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
# MATPLOTLTLIB PLOTTING
import matplotlib.pyplot as plt
import numpy as np
xpoints =np.array([1,8])
ypoints =np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Multiple points
# Draw a line in a diagram from point (1,3) to (2,8) then to (6,1) and finally to position (8,10):
import matplotlib.pyplot as plt
import numpy as np

xpoints =np.array([1, 2, 6, 8])
ypoints =np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default x-points
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
# MATPLOTLIB MARKERS
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o')
plt.show()

# Format strings 
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
# MARKER SIZE AND COLOR
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o', ms=20)
plt.show()

# MARKER COLOR
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, marker ='o', ms=20, mec='r')
plt.show()

# MATPLOTLOTLIB LINE 
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, lineStyle='dashed')
plt.show()

# Line color
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, color='r')
plt.show()

# line width
import matplotlib.pyplot as plt
import numpy as np

ypoints =np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth='20.5')
plt.show()

# Multiple lines
import matplotlib.pyplot as plt
import numpy as np

y1=np.array([3, 8, 1, 10])
y2=np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# MATPLOTLIB LABELS AND TITLE
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90,95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average pulse")
plt.ylabel("calories burnage")

plt.show()

# Set font properties for title and labels
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.title("sports watch data", fontdict=font1)
plt.xlabel("Average pulse", fontdict=font2)
plt.ylabel("calorie burnage", fontdict=font2)

plt.plot(x, y)
plt.show()
# Matplotlib Grid line
# Add grid lines to the plot
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("sports watch data")
plt.xlabel("Average pulse")
plt.ylabel("calorie burnage")

plt.plot(x, y)

plt.grid()

plt.show()

# specify which grid lines to display
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("sports watch data")
plt.xlabel("Average pulse")
plt.ylabel("calorie burnage")

plt.plot(x, y)

plt.grid(axis ='x')

plt.show()

# Display only grid lines for y-axis
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("sports watch Data")
plt.xlabel("Average pulse")
plt.ylabel("calorie burnage")

plt.plot(x, y)

plt.grid(axis='y')

plt.show()

# Set line properties for the grid 
import numpy as np
import matplotlib.pyplot as plt

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports atch Data")
plt.xlabel("Average pulse")
plt.ylabel("calorie burnage")

plt.plot(x, y)

plt.grid(color='green', lineStyle='--', linewidth=0.5)

plt.show()

# Matplotlib subplot

import matplotlib.pyplot as plt
import numpy as np 

x=np.array([0, 1, 2, 3,])
y=np.array("3, 8, 1, 10")

plt.subplot(1, 2, 3)
plt.plot(x, y)

# plot 2:
x=np.array([0, 1, 2, 3])
y=np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()
# Creating scatter plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
# Draw two plots on the same figure:
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
# Colors
# Set your own color of the markers:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()
# Color Each Dot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()
# Colormap
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()
# Include the actual colormap:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()
# set your own size for the markers:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()
# Alpha
# set your own size for the markers
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()
# create random arrays with 100 values for x-points, colors and sizes:
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()

plt.show()

# MATTPLOTLIB BARS
# Draw 4 bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
# Horizontal bars
# Draw 4 horizontal bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

# Bar color
# Draw 4 red bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()

# color Names
# Draw 4 hot pink bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

# Color hex
# Draw 4 bars with a beautiful green color:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()

#Bar width
# Draw 4 very thin bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()

# # Bar height
# Draw 4 very thin bars:
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()
# Matplotlib Histograms
# A Normal Data Distribution by Numpy
import numpy as np

x = np.random.normal(170, 10, 250)

print(x)
# A simple histogram:
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()