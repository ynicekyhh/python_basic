import copy

# copy reference
a = 1
b = a

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)


x[2] = 0
print(x)
print(y)

print('########shallow copy##########')
# shallow copy - x의 ref를 복사함
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)       # false 가 출력
print(x[0] is y[0])

# deep copy - x ref안의 모든 ref까지 다 복사함
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

print('###########deep copy, shallw copy 확인###########')
# 깊은 복사가 복합 객체만을 생성하기 때문에
# 복합객체가 한개만 있을 경우 얕은 복사와
# 깊은 복사의 차이가 없다.
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

# 기본적으로 python 은 thread safe이다.
# iPython이 나와서 tread safe하지 않게 하여 속도를 조금 손봄

# deep copy는 안에 추가/생성 되는 객체들의 값이 계속 바뀌거나 할 때 사용하면 유용함

