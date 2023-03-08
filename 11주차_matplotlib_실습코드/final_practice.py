import pandas as pd

weather = pd.read_csv('/Users/jaeyyoo/python_soongsil/12주차_pandas_실습코드/data/weather.csv')
weather['month']= pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)