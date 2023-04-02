import matplotlib.pyplot as plt
import numpy as np

numX = np.random.randint(0,50,30)
numY = np.random.randint(0,50,30)

plt.scatter(numX, numY, s=50, c="green")
plt.title("scatter makes scatter graph")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.axis([0,50,0,50])
plt.show()