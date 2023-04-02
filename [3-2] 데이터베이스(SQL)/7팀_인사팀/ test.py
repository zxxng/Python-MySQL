import pymysql
import pandas as pd

con = pymysql.connect(host='localhost', user='root', password='220511', db='인사팀', charset='utf8')

cur = con.cursor()

table3 = ['부서명','부서위치','부서장','전화번호'] 

data_add = "'제품개발팀', '본사', '유재영', 12345678"

sql_input = "INSERT INTO  부서 VALUES (" + data_add + ")"

res = cur.execute(sql_input)
data = cur.fetchall()
df_data = pd.DataFrame(data, columns=table3)
print(df_data.to_numpy)


con.commit()
cur.close()
con.close()