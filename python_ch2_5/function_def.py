# 함수 정의
def dummy():
    pass


def my_function():
    print('Hello World')


def time(a, b):
    return a**b


def none():
    return


# 아래처럼 b, a를 리턴하게 되면 tuple로 자동으로 변환되어 리턴함
def swap(a, b):
    return b, a

dummy()
my_function()
print(time(2, 10))
# 아래의 none()은 아무것도 return하지 않으나, python에서는 None 객체를 리턴함
print(none())

a = 10
b = 20
# 여기서는 swap에서 tuple로 packing되어 온 애를 a, b로 unpacking하여 받게 됨
# 많은 객체를 리턴할 수 있음
a, b = swap(a, b)
print(a, b)

# 함수도 객체다
print(dummy, type(dummy))
t = time
print(t(2, 5))

