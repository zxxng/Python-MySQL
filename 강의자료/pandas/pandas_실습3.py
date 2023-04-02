import pandas as pd

df_1 = pd.DataFrame( {'A' : ['a10', 'a11', 'a12'],
                      'B' : ['b10', 'b11', 'b12'],
                      'C' : ['c10', 'c11', 'c12']} , index = ['가', '나',  '다'] )

df_2 = pd.DataFrame( {'B' : ['b23', 'b24', 'b25'],
                      'C' : ['c23', 'c24', 'c25'],
                      'D' : ['d23', 'd24', 'd25']} , index = ['다', '라',  '마'] )

print(df_1.merge(df_2, how='left', ob='B'))
print(df_1.merge(df_2, how='right', ob='B'))
print(df_1.merge(df_2, how='outer', ob='B'))
print(df_1.merge(df_2, how='inner', ob='B'))
