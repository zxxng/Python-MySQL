import pandas as pd

# countrise_df = pd.read_csv('/Users/jaeyyoo/python_soongsil/12주차_pandas_실습코드/data/countries.csv', index_col=0)
# countrise_df['density'] = countrise_df['population']/countrise_df['area']
# print(countrise_df)


weather = pd.read_csv('/Users/jaeyyoo/python_soongsil/12주차_pandas_실습코드/data/weather.csv')
print(weather[weather['최대풍속'] >= 10.0])