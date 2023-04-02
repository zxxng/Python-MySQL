import numpy as np

heights_avg = 175
weights_avg = 70
age_avg = 22
sigma = 10

heights = heights_avg + sigma * np.random.randn(1000)
weights = weights_avg + sigma * np.random.randn(1000)
age = age_avg + sigma * np.random.randn(1000)
