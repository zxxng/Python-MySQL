import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv', encoding='utf-8')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()
means['평균풍속'].plot(kind='bar')

plt.show()