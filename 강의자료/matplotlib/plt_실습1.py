import matplotlib.pyplot as plt

x = [x for x in range(-10, 10)]
y = [2*t for t in x]

plt.plot(x, y, color='blue', marker='o')
plt.axis([-20,20,-20,20])
plt.show()