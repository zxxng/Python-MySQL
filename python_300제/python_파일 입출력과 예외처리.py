# 컴퓨터에 저장된 파일을 읽거나 반대로 파일을 쓸 수 있다.
# 프로그램을 작성하다보면 예외가 발생할 수 있는데 이를 잘 처리하는 것도 중요

# 291 파일 쓰기
stock = open("/Users/jaeng/Desktop/매수종목1.txt", "w", encoding="utf-8")
stock.writelines("005930\n005380\n035420")
stock.close()

# 292 파일 쓰기
stock2 = open("/Users/jaeng/Desktop/매수종목2.txt", "w", encoding="utf-8")
stock2.writelines("005930 삼성전자\n005380 현대차\n035420 NAVER")
stock2.close()

# 293 csv 파일 쓰기

# 294 파일 읽고  list에 저장하기
# inStr = ""
stock = open("/Users/jaeng/Desktop/매수종목1.txt", "r", encoding="utf-8")
lines = stock.readlines()
readList = []
for line in lines:
    code = line. strip("\n")
    readList.append(code)
# while True :
#     inStr = stock.readline()
#     if inStr == "\n" :
#         readList.append(inStr)
#         inStr = ""
#     if inStr == "" :
#         break;
stock.close()

print(readList)

# 295 파일 읽고 딕셔너리 저장하기
stock2 = open("/Users/jaeng/Desktop/매수종목2.txt", "r", encoding="utf-8")
lines = stock2.readlines()
readDict = {}
for line in lines:
    line = line.strip("\n")
    k, v = line.split(" ")
    readDict[k] = v 

print(readDict)
stock2.close()

# 예외처리
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)

# 예외처리 후 리스트 저장
exList = []
for i in per :
    # try:
    #     exList.append(float(per))
    # except:
    #     exList.append(0)
    try:
        v = float(i)
    except:
        v = 0
    exList.append(v)

print(exList)

# 298 특정 예외만 처리하기
try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누기 불가")

# 299 예외의 메시지 출력하기
data = [1, 2, 3]

try:
    for i in range(5):
        print(data[i])
except  IndexError as e:
    print(e)

# 300 try, except, else, finally 구조 사용해보기
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

