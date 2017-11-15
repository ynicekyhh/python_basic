# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# 디렉토리 경로명과 파일명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

first_result = s.split('/')[1:]
print(first_result)

second_result = s.rsplit('/', 1)
print(second_result)

