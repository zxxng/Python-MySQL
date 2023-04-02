inFp, outFp = None, None
inStr = ""

inFp = open("/Users/jaeng/Desktop/python_txt 파일/이진파일.png", "rb")
outFp = open("/Users/jaeng/Desktop/python_txt 파일/테스트.exe", "wb")

while True:
    inStr = inFp.read(1)
    if not inStr:
        break;
    outFp.write(inStr)

inFp.close()
outFp.close()
