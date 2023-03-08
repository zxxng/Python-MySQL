################################(월 기준)
import pandas as pd
weather = pd.read_csv('d:/data/weather.csv', encoding='cp949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)

##############################(일 기준)
# weather['day'] = pd.DatetimeIndex(weather['일시']).day
# means = weather.groupby('day').mean()
# means
##############################(년 기준)
# weather['year'] = pd.DatetimeIndex(weather['일시']).year
# means = weather.groupby('year').mean()
# means

# sum_data = weather.groupby('month').sum()
# print(sum_data)