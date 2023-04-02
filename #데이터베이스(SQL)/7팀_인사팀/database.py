import pymysql
import pandas as pd
from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = False
con = pymysql.connect(host='localhost', user='root', password='220511', db='인사팀', charset='utf8')

cur = con.cursor()

table1 = ['부서명','사번','성명','직급','입사년도','성별']
table2 = ['사번','성명','직급','연봉','평가등급','승진포인트','승진가능여부']
table3 = ['부서명','부서위치','부서장','전화번호']
table4 = ['동호회명','동호회장사번','동호회장','개설일자','월회비','활동횟수']

def table_check(name):
    if name == '직원' :
        return (table1)
    elif name ==  '연봉및평가':
         return (table2)
    elif name == '부서':
        return (table3)
    elif name == '동호회':
        return (table4)

print("안녕하세요. 인사관리 프로그램입니다.")

while True :
    code_query = int(input("수행하려는 조건을 입력해주세요. 1)조회 2)삽입 3)삭제 4)종료 \n"))

    if code_query == 1 :
        table_name = input("조회하고 싶은 테이블명을 입력해주세요. \n")
        if table_name != '직원' and table_name != '연봉및평가' and table_name != '부서' and table_name != '동호회':
            print("잘못된 입력입니다. 처음부터 다시 입력해주세요.\n")
            continue
        table_list = table_check(table_name); print("%s 항목 :" % table_name, table_list)
        table_col = input("조회하고 싶은 항목을 입력해주세요. 조회하고 싶은 항목이 여러개일 경우 ,(콤마)로 구분하여 입력해주세요. \n")
        data_where = input("조회 조건을 입력해주세요. \n")
        if data_where == "" :
            sql_input = "SELECT " + table_col + " FROM " + table_name
        else :
           sql_input = "SELECT " + table_col + " FROM " + table_name + " WHERE " + data_where

        
    elif code_query == 2 :
        table_name = input("데이터를 추가하고 싶은 테이블명을 입력해주세요.\n")
        if table_name != '직원' and table_name != '연봉및평가' and table_name != '부서' and table_name != '동호회':
            print("잘못된 입력입니다. 처음부터 다시 입력해주세요.\n")
            continue
        table_list = table_check(table_name); print("%s 항목 :" % table_name, table_list)
        data_add = input("추가하려는 정보를 형식에 맞게 입력해주세요.\n")
        sql_input = "INSERT INTO " + table_name + " VALUES (" + data_add + ")"
        print("%s 테이블에 데이터 삽입이 완료되었습니다.\n" % table_name)


    elif code_query == 3 :
        table_name = input("데이터를 삭제하고 싶은 테이블명을 입력해주세요.\n")
        if table_name != '직원' and table_name != '연봉및평가' and table_name != '부서' and table_name != '동호회':
            print("잘못된 입력입니다. 처음부터 다시 입력해주세요.\n")
            continue
        table_list = table_check(table_name); print("%s 항목 :" % table_name, table_list)
        data_del = input("삭제할 데이터의 조건을 입력해주세요. (*필수)\n")
        if data_del == "" :
            print("조건을 입력해야합니다. 처음부터 다시 입력해주세요.\n")
        else :
           sql_input = "DELETE FROM " + table_name + " WHERE " + data_del
        print("%s 테이블에 데이터 삭제가 완료되었습니다.\n" % table_name)

           
    elif code_query == 4:
        break

    else :
        print("잘못된 입력입니다. 처음부터 다시 입력해주세요.\n")
        continue
    
    res = cur.execute(sql_input)
    data = cur.fetchall()
    pd.set_option('display.max_rows',None)
    
    df_data = pd.DataFrame(data,columns=[table_list])
    #print(tabulate(df_data, showindex=False, headers=df_data.columns, tablefmt='fancy_grid'))

print("인사팀 프로그램을 종료합니다.")

con.commit()
cur.close()
con.close()