import matplotlib.pyplot as plt

numX = [1,2,3,4,5,6,7,8,9,10]
numY = range(10,0,-1)

plt.scatter(numX, numY, s=50, c="green")
plt.title("scatter makes scatter graph")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()
