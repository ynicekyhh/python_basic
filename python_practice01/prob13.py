# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

num = input()
num = int(num)

odd = 0
even = 0
for n in range(num+1):
    if n & 1 == 1:
        odd += n
    else:
        even += n

if num & 1 == 1:
    print('결과 값', odd, sep=' : ')
else:
    print('결과 값', even, sep=' : ')