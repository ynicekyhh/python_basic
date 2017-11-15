# 논리 연산자
a = 20
b = 30

print(not a > b)
print(a < 30 and a != 30)
print(a < 30 and 'a != 30')
print(a == 30 or a > 30)

# True -> 1, False -> 0 (좋은 코드는 아님)
print(True + 1)
print((a > b) + 1)

# 캐스팅 내장함수
# int()
# bool()
# float()
# byte()
# str()
# 등의 사용이 가능
print(bool(10))

