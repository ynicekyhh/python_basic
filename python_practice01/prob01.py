# 키보드로 정수 수치를 입력 받아 그것이 짝수인지 홀수인지 판별하는 코드를 완성하세요.

import sys

number = input('수를 입력하세요: ')

if number.isdigit():
    if (int(number) % 3) is 0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")
else:
    print('정수가 아닙니다.')
sys.exit(0)