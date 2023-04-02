import shutil
import os
import os.path

shutil.copy("복사할파일경로/파일명", "복사될파일경로/파일명") : 파일 복사
shutil.copytree("복사할디렉토리경로", "복사될디렉토리경로") : 디렉토리 복사
shutil.retree("폴더명") : 폴더 안의 모든 파일 삭제
os.mkdir("폴더명") : 폴더 생성

# 파일 또는 폴더가 존재하는지 확인
os.path.exists("파일명 또는 폴더명")
os.path.isfile('')
os.path.isdir('')

# 파일 삭제
os.remove("file name")

# 파일 크기 확인
os.path.getsize('file name')

