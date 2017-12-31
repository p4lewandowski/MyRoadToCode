import numpy as np
import matplotlib.pyplot as plt

x=(0,1,2)
y = (0, 1, 2)
# Just a figure and one subplot
f, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
plt.show()