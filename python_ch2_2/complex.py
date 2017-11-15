# 복소수 타입의 객체는 실수부 + 허수부로 나뉘며 허수부에는 j 또는 J를 숫자 뒤에 붙힌다.
a = 4 + 5j
print(a, type(a), sep=',')
print(isinstance(a, complex))

# 복소수 연산
b = 7 - 2j
print(a + b)