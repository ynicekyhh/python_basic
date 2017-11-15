
a = 23
print(type(a))
print(isinstance(a, int))

b = 0b1101
c = 0o23
d = 0x23

print(a, b, c, d, sep=' ')

# 3.x 에서는 int와 long이 합쳐졌다.
# 따라서 표현 범위가 굉장히 크다

e = 2 ** 1024
print(e)
print(type(e))

# 변환 함수
print(oct(38))
print(hex(38))
print(bin(38))