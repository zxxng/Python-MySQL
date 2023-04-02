# 파이썬 모듈이란? 파이썬 파일을 의미
# 파이썬은 다양한 분야별로 모듈을 제공. 프로그램 구현에 필요한 모듈의 기초 사용법 익히기!!

# 241 현재 시간
import datetime
now = datetime.datetime.now()
print(now)

# 242 datetime 모듈의 리턴 값
print(type(now))

# 243 timedelta 오늘로부터 5일, 6일, 3일, 2일, 1일 전의 날짜 출력
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

# 244 strftime 
print(now.strftime("%H:%M:%S"))

# 245 strptime
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

# 246 sleep
import time
import datetime


# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247 모듈을 import하는 4가지 방식 ??

# 248 os 모듈  getcwd 함수 - 현재 디렉토리 경로 출력
import os
ret = os.getcwd()
print(ret, type(ret))

# 249 rename 함수 - os모드를 활용한 파일 이름 변경
import os
os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250 numpy arange 함수 - 0.0 부터 5.0까지 0.1씩 증가하는 값
import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)

