# scope test

x = 1


def func(a):
    return a + x
# x는 global이니 참조가능
print(func(10))


def func2(a):
    x = 2
    return a + x

print(func2(10))
print(x)


g = 1
def func3(a):
    # global 키워드를 사용하면 변수의 범위를 설정하게 할 수 있으나 잘 쓰진 않음
    global g
    g = 3
    return a + g

print(func3(10), g)