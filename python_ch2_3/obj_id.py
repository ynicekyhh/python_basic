# Object ID
i1 = 10
i2 = 10

# 아래의 결과를 보면, 상수풀이 존재함을 알 수 있음('10'의 주소값이 동일함)
print(hex(id(i1)), hex(id(i2)))

# l1, l2는 변경 가능한 list니까 주소가 다름
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

# 참고로, 상수풀은 매우 큰 값이 되면 상수풀에서 관리하지 않고, 새로 만들어 사용하는 경우가 있음


# s1, s2는 변경 불가한 값이니 주소가 같음
s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

