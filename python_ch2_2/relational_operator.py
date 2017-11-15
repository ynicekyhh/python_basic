# 객체의 값 대소 비교
print(1 > 3)
print(2 > 4)

print(2 >= 4)
print(2 <= 4)

print(2 == 4)
print(2 != 4)

# 복합관계식도 지원
a = 6
print(0 < a and a < 10) # 이 코드를 더 깔끔하게 사용하라고 밑줄나옴
print(0 < a < 10)

# Python 에서는 기본 연산자 오버라이딩이 가능!(다른 객체 타입의 사칙연산을 할 수 있도록 오버라이딩 제공!)


# 수치형 이외의 객체도 비교가능
print('abcd' > 'abc')
print('test')
print([1, 2, 4] > [1, 2, 3, 5]) # 각각의 원소 하나씩 비교하다가 하나라도 결과가 나오면 끝

# 동질(값)성 비교 ==
# 동일(참조값)성 비교 is

# Python 에서의 a == b 는 JAVA의 a.equals(b)
# Python 에서의 a is b 는 JAVA의 a == b

# Python 에서는 symbolic table이 존재하기 때문에 Call by object reference로 동작한다.
a = 10
b = 20
c = a

print(a == b)
print(a is b)

print(a == c)
print(a is c)

# 논리식의 계산 순서
print([] or 'logical')  # 앞의 []가 false가 되면 or 뒤의 값이 리턴,
print([1] or 'logical') # true면 or니까 뒤의 'logical'을 할 필요가 없고, 앞의 [1]을 리턴

# and는 둘 다 true이면 뒤의 것이 실행, false가 있으면 앞의 것이 실행
print([] and 'logical')
print('logical' and 'operator')
print(None and 1)   # 객체는 비어있으면 None

