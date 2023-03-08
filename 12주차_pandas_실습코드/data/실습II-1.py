import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('d:/data/weather.csv', encoding='cp949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()
means['평균풍속'].plot(kind='bar')

plt.show()