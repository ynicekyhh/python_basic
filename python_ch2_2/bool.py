# 참이나 거짓을 나타내는 True, False 두 상수를 갖는다

a = 1
b = a < 10
print(b, type(b), sep=",")

b1 = True
b2 = False

# c와 같이 true가 1이고, false가 0이란 것을 알 수 있음
print(b1 + 10)
print(b2 + 10)
print(True + True)

if a < 10:
    pass    # if문 안에 쓸 내용이 없으면 pass를 사용!(비어놓으면 에러남)

if a < 10:
    print(a)