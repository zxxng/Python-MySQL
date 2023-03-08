import matplotlib.pyplot as plt

# 실습1
# x = [x for x in range(-10,10)]
# y = [2*t for t in x]

# plt.plot(x,y, 'bo-')
# plt.show()


# 실습2
# import numpy as np
# import random
# res = np.random.randint(0, 50, size=(2,30))

# plt.scatter(res[0],res[1])
# plt.show()

# 실습3

# import numpy as np


# mu1, sigma1 = 10, 2
# mu2, sigma2 = -6, 3

# standard_Gauss = np.random.randn(10000)
# Gauss1 = mu1 + sigma1 * np.random.randn(10000)
# Gauss2 = mu2 + sigma2 * np.random.randn(10000)

# plt.figure(figsize=(10,6))
# plt.hist(standard_Gauss, bins=50, alpha=0.4)
# plt.hist(Gauss1, bins=50, alpha=0.4)
# plt.hist(Gauss2, bins=50, alpha=0.4)
# plt.show()

# 실습4
# import numpy as np

# data = np.random.randn(2, 100)
# fig, axs = plt.subplots(2,2, figsize=(5,5))

# axs[0,0].hist(data[0])
# axs[0,1].plot(data[0],data[1])
# axs[1,0].scatter(data[0],data[1])
# axs[1,1].hist2d(data[0],data[1])

# plt.show()

# month = list(range(7,13))
# new_user = [456, 492, 578, 599, 670, 854]

# fig, axs = plt.subplots(1, 4, figsize=(10,3))

# axs[0].bar(month, new_user)
# axs[1].plot(month, new_user)
# axs[2].scatter(month, new_user)
# axs[3].barh(month, new_user)

# plt.plot(month, new_user)
# plt.show()

# 실습5

plt.legend(('범례1','범례2','범례3'), loc='upper left')