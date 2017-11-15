import sys

x = object()    # refcount가 1
print(type(x))
print(sys.getrefcount(x))   # sys.getrefcount가 x를 참조하니까 여기서는 '2'가 출력되고, getrefcount()를 빠져나가면 참조가 1이 될 것
y = x           # refcount가 2
print(sys.getrefcount(x))


# 레퍼런스값을 줄인다
del x   # x = null 과 같은 의미
print(sys.getrefcount(y))

a = 10
print(sys.getrefcount(a))