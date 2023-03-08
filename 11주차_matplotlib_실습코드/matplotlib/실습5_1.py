#실습 1-1

import matplotlib.pyplot as plt

x = [x for x in range(7, 13)]
y = [456, 492, 578, 599, 670, 854]

plt.plot(x, y)
plt.title("Daehan company speeda net new customers")
plt.xlabel("Month")
plt.ylabel("User")

plt.show()
