
from matplotlib import pyplot as plt 
 

years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

x_range = range(len(years))
plt.bar(x_range, ko, width = 0.25)
plt.bar(x_range, jp, width = 0.25)
plt.bar(x_range, ch, width = 0.25)

plt.title("GDP per capita")   
plt.ylabel("dollars")    
 

plt.xticks(range(len(years)), years) 
plt.show()

import numpy as np

x_range = np.arange(len(years))
plt.bar(x_range + 0.0, ko, width = 0.25)
plt.bar(x_range + 0.3, jp, width = 0.25)
plt.bar(x_range + 0.6, ch, width = 0.25)

plt.title("GDP per capita")   
plt.ylabel("dollars")          
 

plt.xticks(range(len(years)), years) 
plt.show()
