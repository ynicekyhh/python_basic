# 치환문의 예

a = 1
b = a + 1
print(a, b, sep=',')


# 1 + 3 = c 에러
e = 3; f = 5 + 2    #되긴 하지만 지양
print(e, f)

# 여러 변수를 한 번에 치환
e, f = 3, 7
print(e, f, sep=',')

# 하나의 값을 여러 변수에 대입하기
x = y = z = 1

# 값 교환
f, e = e, f
print(e, f, sep=',')

# 동적 타이핑
a = 1
print(type(a))
a = 'hello'
print(type(a))
