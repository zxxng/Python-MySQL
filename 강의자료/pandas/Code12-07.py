import pandas as pd

df_my_index = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/countries.csv',encoding="utf-8", index_col = 0)
df_no_index = pd.read_csv('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/countries.csv')
print(df_my_index['population'])
print(df_no_index['population'])