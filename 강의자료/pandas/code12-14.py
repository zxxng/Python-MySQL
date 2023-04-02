import pandas as pd

weather = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv', index_col = 0, encoding='utf-8')
print(weather.describe())
print('평균 분석 -----------------------------')
print(weather.mean())
print('표준편차  분석 -----------------------------')
print(weather.std())
