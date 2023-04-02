# code 11_10_2
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(range(10), 'r')
ax2.plot(range(10), 'b')
ax3.plot(range(10), 'g')
ax4.plot(range(10), 'k')
plt.show()