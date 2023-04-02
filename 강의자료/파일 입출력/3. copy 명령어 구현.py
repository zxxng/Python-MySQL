inFp, outFp = None, None
inStr = ""

inFp = open("/Users/jaeng/Desktop/python_txt 파일/data1.txt", "r", encoding='UTF8')
outFp = open("/Users/jaeng/Desktop/python_txt 파일/data3.txt", "w", encoding='UTF8')

inList = inFp.readlines()
for i in inList:
    outFp.writelines(i)

inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")