import pandas as pd
weather = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv', index_col = 0, encoding='utf-8')
weather.fillna(0, inplace = True) # Fulas로 놔두는게 좋다 .

print(weather.loc['2012-02-11']) # 행찾기 명령어