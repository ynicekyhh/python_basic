import sys
# import mymath     # 경로를 찾을 수 없으니 당연히 import안됨
print(sys.path)

# 1번째 방법
# pythonpath에 경로를 동적으로 추가해주는 방법(추천하지 않음)
# sys.path.append('/bigdata/PycharmProjects/python_modules')
# import mymath
# print(sys.path)
# print(mymath.add(10, 20))

# 2번째 방법은 환경변수에 추가하는 방법

# 3번째 방법은 pycharm 세팅에서 설정
# setting -> project -> project interpreter -> setting -> add -> 원하는 위치 추가
import mymath

print(mymath.add(10, 20))
print(mymath.pi)

