# 인수의 전달 방식


def f(t):
    t = 20


a = 10
f(a)
print(a)


# tuple은 immutable, 새로운 reference를 가리키게 함
def h(t):
    t = (10, 20, 30)


a = (1, 2, 3)
h(a)
print(a)


# mutable은 같은 reference를 수정함
def g(t):
    t[0] = 0


a = [1, 2, 3]
g(a)
print(a)