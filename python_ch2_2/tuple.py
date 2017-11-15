# 튜플 생성 및 연산

# 튜플 생성 시에 괄호가 들어가기 때문에, if문 등에서 문제가 될 수 있으니 괄호를 빼버림
t = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3, 4

print(t4)
print(type(t4))

print(type(t), type(t2), sep=' ')

# 인덱싱
print(t3[-2], t3[-1], t3[0], t3[1], t3[2])

# 슬라이싱
t4 = t3[1:3]
print(t4)
t6 = t3     # 객체의 reference를 복사함
t5 = t3[:]  # 새로운 tuple 객체를 만들어 t5에 리턴함
print(t5, type(t5), sep=', ')
print(t6)

# 반복
t7 = t3 * 2
print(t7)

# + 연결
t8 = t3 + (3, 4, 5)
print(t8)

# 길이
print(len(t8))

# 확인
print(5 in t8)
print(5 not in t8)

# 튜플은 변경 불가능
# t = ('apple', 'banana', 10, 20)
# t[2] = t2[2] + 20

# 내장 함수 list(), tuple(), set()를
# 사용해서 서로서로 변환이 가능하다.
t = (1, 2, 3, 3)
s = set(t)
print(s, type(s))
l = list(t)
print(l, type(l))

# swap
x = 10
y = 20
x, y = y, x
print(x, y)

# 메서드가 많지 않다.
print(t.index(2))   # 파라미터 값이 들어있는 index위치 값 리턴
print(t.index(3))
print(t.count(3))

# 순환문
for i in t:
    print(i, end=' ')