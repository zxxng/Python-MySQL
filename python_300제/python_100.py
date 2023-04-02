## 초보자를 위한 파이썬 300제

# 파이썬 시작하기
# 001 print 기초
from fileinput import close
from operator import inv, invert
import re
from sre_constants import IN
from turtle import st
from xml.dom.expatbuilder import InternalSubsetExtractor


print("Hello World");

# 002 print 기초
print("Marry\'s cosmetics");

# 003
print('신씨가 소리질렀다. "도둑이야"');

# 004
print('"C:\Windows"');

#006 
print("오늘은", "일요일");

#007
print("naver", "kakao", "samsung", sep=";")

#009
print("first", end="");print("second")


# 파이썬 변수 사용하기
# 011
삼성전자 = 50000;
print("총 평가금액 = %d" % (삼성전자*10))

# 012
s = "hello";
t = "python";
print("%s! %s" % (s, t))

# 013 형변환
num_str = "720";
num_int= int(num_str)
print(num_int+1, type(num_int))

# 019
year = "2020"
calc = int(year)
print(calc-3, calc-2, calc-1, sep=" ")

# 020
won = 48584; month = 36
print("에어컨 총 금액은 %d원 입니다" % (won*month))

# 파이썬 문자열
# 021 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 [시작인덱스:끝인덱스:오프셋]
string1 = "홀짝홀짝홀짝"
print(string1[0::2])

# 024
string = "PYTHON"
print(string[-1::-1])

# 025 문자열 치환
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-", " ")
print(phone_number)

# 026 문자열 다루기
phone_number = phone_number.replace(" ", "")
print(phone_number)

# 027
url = "http://sharebook.kr"
url = url.split('.')
print(url[-1])

# 029 
string3 = 'abcdfe2a354a32a'
string3 = string3.replace('a', 'A')
print(string3)

## 문자열은 변경할 수 없는 자료형으로 메서드 사용시 원본은 그대로 둔 채 변경된 새로운 객체 리턴

# 033
print('-' * 80)

# 034
t1 = 'python'; t2 = 'java';
# print((t1+t2)*4, sep = " ")
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)

# 035
name1 = "김민수"; age1 = 10; name2 = "이철희"; age2 = 13
print("이름: %s 나이: %d\n이름: %s 나이: %d" % (name1, age1, name2, age2))

# 036  format() 메서드는 타입과 상관없이 값이 출력될 위치에 {} 적으면 됨
print("이름: {} 나이: {}\n이름: {} 나이: {}".format(name1, age2, name2, age2))

# 037 f-strin (python 3.6  부터 지원)
#print(f"이름: {name1} 나이: {age}\n이름: {name2} 나이: {age2}")

# 038
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",","")
상장주식수 = int(상장주식수)
print(상장주식수, type(상장주식수))

# 039
분기 ="2020/03(E) (IFRS연결)"
분기 = 분기.split("(")
print(분기[0]) # or print(분기[:7])

# 040 strip 메서드
data = "    삼성전자    "; data = data.strip()
print(data)


# 041 ~ 050 메서드 활용
# 041 upper() : 대문자 변환
# 042 lower() : 소문자 변환
# 043 capitalize() : 대소문자 변환
# 044 endswith() : 해당 문자로 끝나는지 확인
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
# 045 'xlsx' 또는 'xls'
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
# 046 startswith() : 해당 문자로 시작하는지 확인
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
# 047 split() : 구분자로 문자열 나누기
# 050 rstrip() : 오른쪽 공백 제거 / stripn() : 공백 제거


# 파이썬 리스트 : 순서가 있고 수정 가능한 자료구조
# 051 리스트 생성
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 052 리스트 원소 추가
movie_rank.append("배트맨")
print(movie_rank)

# 053 리스트 중간에 원소 추가
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054  리스트 원소 삭제
movie_rank.remove("럭키") #  or del movie)rank[3]
print( movie_rank)

# 055 리스트 원소 삭제
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)

# 056 리스트 합
lang1 = ["c", "c++", "java"]; lang2 = ["python", "go", "c#"];
langs = lang1 + lang2;
print(langs)

# 057 리스트 최대 최솟값
nums = [1,2,3,4,5,6,7]
print("max: %d\nmin: %d" % (max(nums), min(nums)))

# 058 
nums = [1,2,3,4,5]
print(sum(nums))
ret = 0;
for i in nums:
    ret += i;
print(ret)

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1,2,3,4,5]
print(sum(nums) / len(nums))

# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
print(nums[::-1])

# 064
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066 ~ 068 join 메서드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))
print("\n".join(interest))

# 069 split
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 070 오름차순 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort() # or data = sorted(data)
print(data)


# 파이썬 튜플 : 순서가 있지만 수정 불가능한 자료구조
# 071 비어있는 튜플 생성
my_variable = ()

# 072
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073
one = (1, )

# 074 : 튜플은 수정 불가능한 자료구조로 오류 발생
t = (1, 2, 3)
# t[0] = 'a'

# 075  괄호 없이도 선언 가능
t2 = 1, 2, 3, 4
print(type(t2))

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

# 077 튜플 -> 리스트 변환
tup_interest = ("삼성전자", "LG전자", "SK Hynix")
new_interest = list(tup_interest)

# 078 리스트 -> 튜플 변환
li_interest = ['삼성전자', 'LG전자', 'SK Hynix']
new2_interest = tuple(li_interest)


# 079 튜플 언패킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
data = tuple(range(2, 100, 2))
print( data )


# 파이썬 딕셔너리 : 순서는 없지만 key, value 형대로 저장됨. key는 데이터의 레이블을 저장하는 용도로 자주 사용
# 081 ~ 083 별 표현식 - stat expression
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

_, _, *valid_score = scores
print(valid_score)

_, *valid_score, _ = scores
print(valid_score)

# 084 빈 딕셔너리 생성
temp = { }

# 085 ~ 090
ice = { "메로나":1000, "폴라포": 1200, "빵빠레":1800}
# 딕셔너리 원소 추가
ice["죠스바"] = 1200; ice["월드콘"] = 1500
print(ice)
# 딕셔너리 키에 상응하는 벨류 출력
print("메로나 가격: %d" % ice["메로나"])
# 딕셔너리 벨류 수정
ice["메로나"] = 1300
print(ice)
# 딕셔버리 삭제
del ice["메로나"]
print(ice)

# 091 ~ 096
inventory = {"메로나": [300, 20], "비비빅":[400,3], "죠스바":[250, 100]}
print("%d원" % inventory["메로나"][0])
print("%d개" % inventory["메로나"][1])
inventory["월드콘"] = [500, 7]
print(inventory)

inventoryList = list(inventory.keys())
print(inventoryList)

inventoryList2 = list(inventory.values())
print(inventoryList2)

# 097 values 메서드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

# 098 update 메서드
new_product = {'팥빙수':2700, '아맛나':1000}
#icecream = icecream + new_product
icecream.update(new_product)
print(icecream)

# 099 zip과 dict
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)