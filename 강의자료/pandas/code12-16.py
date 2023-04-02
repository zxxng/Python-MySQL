import pandas as pd
weather = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv', index_col = 0, encoding='utf-8')
missing_data = weather[weather['평균풍속'].isna()]
print(missing_data)