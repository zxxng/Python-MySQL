################################(월 기준)
import pandas as pd
weather = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv', encoding='utf-8')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)

##############################(일 기준)
# weather['day'] = pd.DatetimeIndex(weather['일시']).day
# -> 데이트 타입으로 만들어야 시계열 자료형 생성 가능
# means = weather.groupby('day').mean()
# means
##############################(년 기준)
# weather['year'] = pd.DatetimeIndex(weather['일시']).year
# means = weather.groupby('year').mean()
# means

# sum_data = weather.groupby('month').sum()
# print(sum_data)