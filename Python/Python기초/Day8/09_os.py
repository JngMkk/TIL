# 디렉토리 생성
import os
os.mkdir('log')
os.mkdir('log2')

# 디렉토리 삭제
import shutil
shutil.rmtree('log')
shutil.rmtree('log2')

# 디렉토리 확인 후 디렉토리 생성
if not os.path.isdir('log'):
    os.mkdir('log')
shutil.rmtree('log')

# 디렉토리 목록 보기
for dirname, subdir, fnames in os.walk('C:/Users/[]/Desktop/TIL/Python'):
    print(dirname)      # 상위 디렉토리
    print(fnames)       # 파일이름

# 파일 또는 디렉토리 존재 여부 확인
print(os.path.exists('C:/Users/[]/Desktop/TIL'))     # True/False

# 디렉토리인지 파일인지 구분
print(os.path.isdir('C:/Users/[]/Desktop/TIL'))      # True/False
print(os.path.isfile('C:/Users/[]/Desktop/TIL'))     # True/False

# 파일 삭제
os.remove('C:/Users/[]/Desktop/TIL/hi.py')

# 파일 크기 확인
print(os.path.getsize('C:/Users/[]/Desktop/TIL'))
