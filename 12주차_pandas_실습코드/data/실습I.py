import csv
import matplotlib.pyplot as plt

f = open('c:/temp/weather.csv')
data = csv.reader(f)
header = next(data) # 헤더제거

monthly_wind = list(range(12))
days_counted = [x for x in range(12)]

for row in data:
    month = int(row[0][5:7]) # 일시에서 월 데이터만 추출 2010-"08"-01
    if row[3] != '': # 공백이 아니면 바람이 붐
        wind = float(row[3]) # wind에 최대풍속값 담기
        monthly_wind[month-1] += wind # 월에 해당아는 인덱스에 풍속값 더하기 -> 누적되는 수
        days_counted[month-1] += 1 # 월에 분 풍속 일수를 세기 위한 변수


for i in range(12):
    monthly_wind[i] /= days_counted[i] # 총 풍속값을 바람이 분 날짜 일수로 나누어서 평균 확인

plt.plot(monthly_wind, 'blue')
plt.show()

f.close()