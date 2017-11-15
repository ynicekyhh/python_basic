# 기본 인수 값


def incr(a, step=1):
    return a + step

# 아래처럼 arguments를 다 설정하지 않아도 default값을 가질 수 있다.
print(incr(10))
print(incr(10, 10))


# 기본값이 있는 파라미터를 앞에다 두면, 함수 호출 시 파라미터가 생략되면 어떤놈에게 값을 세팅할지 알 수 없으니 에러
# def incr(step=1, a):
#     return a + step
# def incr(step=1, a=10):       # <-이런식으로 모든 파라미터에 기본값을 설정하면 사용 가능


# 키워드 인수
def area(width, height):
    return width*height


# 아래와같이 파라미터 이름에다 직접 값을 넣는 경우는 파라미터 순서를 어겨도 무방하며, 앞의 파라미터 이름은 생략 가능하다.
print(area(10, 20))
print(area(width=10, height=20))
# print(area(width=10, 20))     # error
print(area(10, height=20))


# 키워드 인수 + 기본 인수
def area2(width=0, height=0):
    return width*height

print(area2())
print(area2(height=10))


# 가변 인수 - *arg는 몇 개의 파라미터가 오든 다 받을 수 있다.
def varg(a, *arg):
    print(a, arg)

varg(1)
varg(1, 2)
varg(1, 2, 3, 4, 5, )

# c의 printf
print('%s, %d' % ('hello', 10))


# 아래처럼 c스타일로 printf를 정의해서 사용 가능
def printf(f, *arg):
    print(f % arg)

printf("%s, %d", "hello", 10)


# 정의되지 않은 파라미터 받기
def f(width, height, **kw):     # dictionary로 받음
    print(width, height, kw)

f(10, 20, depth=30, dimension=40)


def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)
# 아래처럼 이름과 값을 설정하면 dictionary로, 설정하지 않으면 가변 변수로 설정됨
g(10, 20, 30, 40, 50, 60, 70, c=90, d=100)


# 튜플/사전 파라미터
def h(name, age, height):
    print(name, age, height)

# tuple 넘기기
t = ('둘리', 10, 145)
h(*t)

# dictionary 넘기기
d = {'name':'마이콜', 'age':25, 'height':182}
h(**d)