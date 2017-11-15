# 파이썬 클래스 정의 테스트
class MyString:
    pass

s = MyString()
print(type(s))
print(MyString.__bases__)       # MyString의 부모

# s2가 가지는 ''는 str로 built-in 객체니까 __main__이 표시되지 않음
s2 = ''
print(type(s2))
print(str.__bases__)

# 내장(str)되어 있는 class 는 확장시킬 수 없음
# s2.a = 10
# print(s2.a)

# 내가 만든 객체는 확장 가능하나 일반적으로 사용하지 않음(가독성 등의 문제)
# s.a = 10
# print(s.a)

