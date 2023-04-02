import matplotlib.pyplot as plt
import numpy as np

n_bins = 50
standard_Gauss = np.random.randn(10000)
arr1_Gauss = 10 + 2 * np.random.randn(10000)
arr2_Gauss = -6 + 3 * np.random.randn(10000)

plt.hist(standard_Gauss, n_bins, histtype='bar', color='blue', alpha=0.3)
plt.hist(arr1_Gauss, n_bins, histtype='bar', color='red', alpha=0.3)
plt.hist(arr2_Gauss, n_bins, histtype='bar', color='green', alpha=0.3)
plt.show()