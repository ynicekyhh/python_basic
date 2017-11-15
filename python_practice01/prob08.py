# 키보드에서 5개의 정수를 입력 받고 평균을 구하는 프로그램을 작성하시오
import sys

l = []
s = 0

l.append(int(input('> ')))
l.append(int(input('> ')))
l.append(int(input('> ')))
l.append(int(input('> ')))
l.append(int(input('> ')))

for data in l:
    s += data

avg = s / 5

print('{0}: {1}'.format('평균', avg))