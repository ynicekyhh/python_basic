import math
import mymath

print(math.pi)
print(mymath.pi)


x = 1


def f():
    y = x + 1       # y를 embedded variable라 한다.
    print(x)

    def g():
        a = y + 1   # a또한 embedded variable

    for i in range(10):
        g()
        print(y)

f()