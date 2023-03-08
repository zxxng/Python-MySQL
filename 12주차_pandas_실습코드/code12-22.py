import pandas as pd

countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
sorted = countries_df.sort_values('population')
print(sorted)

##################################################
countries_df = pd.read_csv('d:/data/countries.csv', index_col = 0)
countries_df.sort_values('population', inplace = True)
print(countries_df)
####################################################
countries = pd.read_csv('d:/data/countries.csv', index_col = 0)
countries.sort_values(['population', 'area'], ascending=False, inplace = True)
print(countries)

contrise_df = pd.read_csv('way', index_col = 0 , encoding='CP949')
