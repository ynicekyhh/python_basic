# 심볼 테이블 내용 확인

g_a = 1
g_b = 'symbol'

# if문이나 for문 안의 변수들이 로컬이 아니라 글로벌 범위에 존재하게 된다.(JAVA 범위가 다르니 유의할 것)
for i in range(5):
    l_c = 3
    l_d = 'python'
    print(locals())


def f():
    l_a = 2
    l_b = 'table'
    print(locals())


f()
print(locals())
print(globals())

print('##############Class#############')


# class나 funtion은 두 줄을 띄워야 함
class MyClass:
    x = 10
    y = 20
    print(locals())

# 0. 내장 타입 객체는 네임스페이스 접근 금지
# 더 확장 불가
# print(g_a.__dict__)   # 일반 상수 객체는 __dict__(namespace 인 symbolic table을 보여주는 것)는 존재하지만 접근 불가
# g_a.k = 'hello'   # 이것 또한 에러나리
# print(print.__dict__) # print는 내장 함수니까 당연히 확장도 불가하고 왼쪽 처럼 사용할 수 없다.
# print.k = 'hello'
 
# 1. 클래스 객체
print(MyClass.__dict__)

# 2. 정의된 함수 객체
f.k = 'hello'
print(f.__dict__)

# 3. 인스턴스 객체
o = MyClass()
# 아래 o.__dict__는 비어있는 것으로 나옴...(o는 비어있으니까)
print(o.__dict__)
# o.x는 o class안에 x가 없으니까 froto type인 MyClass의 정의부로 가서 x를 찾음
print(o.x)

o.x = 100
print(o.x)

