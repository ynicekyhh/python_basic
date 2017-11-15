# 다른 언어에서처럼 소수점을 포함하거나 e나 E로 지수로 표현할 수 있다.

a = 1.2
print(type(a))
print(isinstance(a, float))
print(a.is_integer())

b = 3e3 # 3000
print(b)
c = -0.2e-4
print(c)

# 객체 함수 is_integer()는 실수 타입 객체의 값이 정수인지 판별한다.
b = 3.0
print(b.is_integer())
