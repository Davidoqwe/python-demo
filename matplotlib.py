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