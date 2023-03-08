#실습 1-2

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 4, figsize=(10, 3))


x = [x for x in range(7, 13)]
y = [456, 492, 578, 599, 670, 854]

ax[0].bar(x, y)
ax[1].plot(x, y)
ax[2].scatter(x, y)
ax[3].barh(x, y)

plt.show()
