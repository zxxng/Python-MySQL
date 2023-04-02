import os

inFp = None #입력파일
inList, inStr = [],"" #읽어온 문자열
idx = 1

fName = input("파일명을 입력하세요 : ")
if os.path.exists(fName):

    inFp = open(fName, "r", encoding="UTF8")
    inList  = inFp.readlines()
    for i in inList:
        print(i, end="")

    inFp.close()
else:
    print("%s 파일이 없습니다." % fName)

# while True:
#     inStr = inFp.readline()
#     if inStr == "" :
#         break;
#     print("%d: %s" % (idx, inStr), end="")
#     idx += 1

# read() : 파일 전체를 읽어 하나의 문자열에 저장
# readline() : 파일의 한줄을 가져와 하나의 문자열로 저장
# readlines() : 파일 내용 전체를 가져와 리스트로 반환. 각 줄은 문자열 형태로 리스트의 요소로 저장


