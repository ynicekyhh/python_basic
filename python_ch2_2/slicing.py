# 슬라이싱 테스트
# [시작옵셋:끝옵셋]
# 옵셋은 생략 가능

a = 'abcdef'

# 시작위치와 끝위치 사이 잘라내는 것
print(a[1:3])

# 1부터 끝까지..
print(a[1:])

# 처음부터 끝까지
print(a[:])

# 범위를 넘어서면 범위 내 값으로 조정
print(a[-100:100])

# 맨 오른쪽 값을 제외하고
print(a[:-1])

# 맨 오른쪽 두 개값을 제외하고
print(a[:-2])

# 확장 슬라이싱
# [start:stop:step]
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::2])