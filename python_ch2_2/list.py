# 리스트 생성과 연산

l1 = []
l2 = [1, 2, 'python']
print(type(l2))

# 인덱싱
print(l2[-2], l2[-1], l2[0], l2[1], l2[2])

# slicing
print(l2[1:3])
print(l2[:])

# repeating
print(l2 * 2)

# concat(+)
print(l1 + [1, 2, 3])
print(l1 + l2)

# length
print(len(l2))

# exist
print(5 in l2)
print('python' in l2)

# delete - 진짜 메모리에서 객체를 날려버림
del l2[0]
print(l2)

# mutable sequence
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 10
print(a)

# replace with slicing
a = [1, 12, 123, 1234]

a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

# 삽입
a[1:1] = [15]
print(a)

# delete with slicing
a = [1, 12, 123, 1234]

a[1:2] = []
print(a)

a[0:] = []
print(a)

# insert with slicing
a = [1, 12, 123, 1234]

a[1:1] = ['A']
print(a)

a[len(a):] = [12345]
print(a)

a[:0] = [-12, -1, 0]
print(a)

# 메서드
a = [1, 2, 3]
print(a)

a.append(5)
print(a)

a.insert(3, 4)
print(a)

print(a.count(2))

a.reverse()
print(a)

# 역순이니까 올림차순으로 다시 정렬
a.sort()
print(a)

a.remove(5)
print(a)

a.extend([5, 6, 7, 8, 9, 10])
print(a)

# using as stack
stack = []
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)

# using as queue
q = [1, 2]

q.append(3)
q.append(4)
q.append(5)

print(q)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print(q)
print("----------l3")
# sort() : 내장된 알고리즘
l3 = [1, 5, 3, 9, 8, 4, 2, 12]
l3.sort()
print(l3)

# 역순
l3.sort(reverse=True)
print(l3)

# 키값 기반의 사용자 정의 정렬하기 - str일 때 정수형과 숫자 정렬 방식이 다름
l3.sort(key=str, reverse=False)
print(l3)

l3.sort(key=int)
print(l3)

def f(i):
    return i % 3

l3.sort(key=f)
print(l3)

# cf. sorting 내장 함수
l4 = sorted(l3, key=f)
print(l4)