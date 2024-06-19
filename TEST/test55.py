import os

# 파일명 정의
file_name = '금일 회수건.txt'

# 파일에 "test" 문자열 출력
with open(file_name, 'w') as file:
    file.write('test')

# 메모장으로 파일 열기 (Windows 환경)
os.system(f'notepad {file_name}')
