# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전,
# 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

import sys

money = input('수를 입력하세요: ')
money = int(money)
print('{0} : {1}{2}'.format('50000원', int(money/50000), '개'))
money %= 50000
print('{0} : {1}{2}'.format('10000원', int(money/10000), '개'))
money %= 10000
print('{0} : {1}{2}'.format('5000원', int(money/5000), '개'))
money %= 5000
print('{0} : {1}{2}'.format('1000원', int(money/1000), '개'))
money %= 1000
print('{0} : {1}{2}'.format('500원', int(money/500), '개'))
money %= 500
print('{0} : {1}{2}'.format('100원', int(money/100), '개'))
money %= 100
print('{0} : {1}{2}'.format('50원', int(money/50), '개'))
money %= 50
print('{0} : {1}{2}'.format('10원', int(money/10), '개'))
money %= 10
print('{0} : {1}{2}'.format('5원', int(money/5), '개'))
money %= 5
print('{0} : {1}{2}'.format('1원', int(money/1), '개'))
