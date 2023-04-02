import csv

f = open('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv',encoding="utf-8")
data = csv.reader(f)
header = next(data) # 헤더 제거

max_wind = 0.0

for row in data :
    if row[3] == '':
        wind = 0
    else :
        wind = float(row[3])
    if max_wind < wind :
        max_wind = wind
print('지난 10년간 울릉도의 최대 풍속은 %fm/s' % max_wind)
    

f.close()