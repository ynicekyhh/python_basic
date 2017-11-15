# packing 은 tuple만 가능하다.
t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking tuple
a, b, c, d = t
print(a, b, c, d)

# 아래는 packing과 unpacking이 동시에 이뤄짐
a, b, c, d = 10, 20, 30, 'python'

# unpacking error
# a, b = (10, 20, 30, 40)

# unpacking extended
a, *b = (1, 2, 3, 4, 5)
print(a)
print(b, type(b), sep=' ')

*a, b = (1, 2, 3, 4, 5)
print(a)
print(b)

a, *b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
