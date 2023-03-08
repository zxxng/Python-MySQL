import pandas as pd
weather = pd.read_csv('/Users/jaeyyoo/python_soongsil/12주차_pandas_실습코드/data/weather.csv', index_col = 0)
missing_data = weather[weather['평균풍속'].isna()]
print(missing_data)