# Code12-01

import csv

f = open("d:/source/weather.csv")
data = csv.reader(f)
for row in data:
    print(row)
f.close()

# Code12-02

import csv

f = open("d:/source/weather.csv")
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close()

# Code12-03

import csv

f = open("d:/source/weather.csv")
data = csv.reader(f)
header = next(data)
for row in data:
    print(row[3], end=",")
f.close()

# Code12-04

import csv     
 
f = open('d:/data/weather.csv')  
data = csv.reader(f)             
header = next(data)

max_wind = 0.0
for row in data:                 
    if row[3] == '' :             
        wind = 0
    else :
        wind = float(row[3])    
    if max_wind < wind :       
        max_wind = wind        

print('지난 10년간 울릉도의 최대풍속중 최대값은 ', max_wind, 'm/s')

# Code12-05

import numpy as np
import pandas as pd
series = pd.Series([1, 3, 4, np.nan, 6, 8])
series

# Code12-06

name_series = pd.Series(['김수안', '김수정', '박동윤', '강이안', '강지안'])
age_series = pd.Series([19, 23, 22, 19, 16])
gender_series = pd.Series(['여', '여', '남', '여', '남'])
grade_series = pd.Series([4.35, 4.23, 4.25, 4.37, 4.25])
print(name_series, age_series, gender_series, grade_series)

# Code12-07

import pandas as pd

df_my_index = pd.read_csv("d:/source/countries.csv", index_col = 0)
df_no_index = pd.read_csv("d:/source/countries.csv")
print(df_my_index['population'])   
print(df_no_index['population'])

# Code12-09

import pandas as pd
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
plt.show()

# Code12-10

import pandas as pd
import matplotlib.pyplot as plt 

weather = pd.read_csv("d:/source/weather.csv", index_col = 0, encoding = 'cp949')
weather['평균 풍속'].plot(kind='hist', bins=33)
plt.show()


# Code12-11

countries_df.head()
countries_df[:3]

# Code12-12

import pandas as pd

countries_df = pd.read_csv("d:/source/countries.csv", index_col = 0)
countries_df['density'] = countries_df['population'] / countries_df['area']
print(countries_df)

# Code12-13

import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='CP949')
print(weather.describe())
