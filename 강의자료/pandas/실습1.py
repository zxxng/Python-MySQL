import csv

f = open('/Users/jaeng/[3-2] 프로그래밍실전(python)/강의자료/pandas/weather.csv',encoding="utf-8")
data = csv.reader(f)
header = next(data) # 헤더 제거

monthly_wind = [x for x in range(12)]
days_counted = [x for x in range(12)]

for row in data :
    month = int(row[0][5:7])
    if row[3] != '':
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_counted[month-1] += 1
print(monthly_wind,"\n", days_counted)

for i in range(12):
    monthly_wind[i] /= days_counted[i]

plt.plot()???
    

f.close()