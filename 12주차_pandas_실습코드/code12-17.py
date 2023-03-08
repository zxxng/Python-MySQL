import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', index_col = 0, encoding='cp949')
weather.fillna(0, inplace = True)

print(weather.loc['2012-02-11'])