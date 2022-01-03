# 파일 압축 및 풀기
import zipfile

# 파일 압축
new = zipfile.ZipFile('C:/Users/JngMK/Desktop/TIL/Python/Python\ 기초/Day8.zip', 'w')
new.write('C:/Users/JngMK/Desktop/TIL/Python/Python\ 기초/Day8/5_file.py', compress_type = zipfile.ZIP_DEFLATED)
new.close()

# 압축 풀기
ext = zipfile.ZipFile('C:/Users/JngMK/Desktop/TIL/Python/Python\ 기초/Day8.zip', 'r')
ext.extractall('C:/Users/JngMK/Desktop/TIL/Python/Python\ 기초/Day8')
ext.close()