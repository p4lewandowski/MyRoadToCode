import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fig, ax = plt.subplots()
plt.style.use('ggplot')
data = np.random.randn(50)
plt.plot(data)


plt.show()