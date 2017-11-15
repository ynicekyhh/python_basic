# 한 줄 문자열 정의
s = ''
str1 = 'Hello World'

print(type(s), type(str1))

# 여러줄 문자열 정의
# '"'가 3개 있으면 여러 줄 string을 지원하나, 주석으로도 사용 가능하다
str2 = """ABCDEFG
abcdefg
가나다라마바사
123456789
"""

print(str2)

# escape
print('Hello\nWorld\nI Say "hello World"')
print("Hello\nWorld\nI Say \"hello World\"")

#
# sequence 타입이 가지는 공통적 연산
#
str1 = 'Hello World'
str2 = 'Hello World'

# 인덱싱(indexing)
print(str1[0], str1[1], str1[2], sep=',' )


# 슬라이싱(slicing)
print(str1[2:5])
print(str1[2:])

# 연결(+)
print(str1 + str2)
# TypeError - str의 '+' 연산은 python에선 __add__를 override해서 구현해 놓았을 텐데, string형만 + 연산이 되도록 구현되어 있다.
# print(str1 + 10)

# 반복(*)
print(str1 * 3)

# len() 함수
print(len(str1))

# in, not in 연산 - 존재 유무 확인
print('S' in str1)
print('S' not in str1)

# 변경 불가능(immutable)
# str1[0] = 'Q'

print('-------------------------------------------------')
# formatting
name = "둘리"
age = 20
# print('name:' + name + ',age:' + 20)
print('name:' + name + ',age:' + str(20))

print('name:' + format(name, 's') + 'age:' + format(age, 'd'))

f = 'name: %s, age: %d'
print(f % ('둘리', 20))

u1 = ('둘리', 10)
u2 = ('마이콜', 20)

s = 'name: %s, age: %d'
print(s % u1)
print(s % u2)

# 대소문자 관련 메소드
s = 'i like python'

print(s.upper())
print(s.lower())
print(s.capitalize())   # 첫 글자만 upper
print(s.title())        # 단어의 첫 글자들만 upper

# 검색 관련
print("검색관련============================")
s = 'I Like Python, I Like Java Also'

print(s.count('Like'))
print(s.find('Like'))
print(s.find('Like', 5))
print(s.rfind('Like'))

# 검색 실패 시
print(s.find('JS'))
# 실패시 예외 발생
# print(s.index('JS'))

# Python에서 method overload의 개념은 없고, 가변인수라는 개념이 존재함(인자를 다양하게 줄 수 있음)
print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))

# 편집과 치환
s = '   spam and ham    '
print('---' + s.strip() + '---')    # 공백과 치환
print('---' + s.rstrip() + '---')
print('---' + s.lstrip() + '---')

s = '<><abc><><defg><><>'
print(s.strip('<>'))    # '<>'패턴으로 없애는 것이 아니라, '<'와 '>를 문자 가운데를 제외하고 다 없앰

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리와 결합
s = 'spam and ham'
# t = s.split('and')  # t는 list로 저장된다.
t = s.replace(' ', '').split('and')
print(t)

t2 = ":".join(t)    # ''.join(t) 이면 '+' 연산과 같은 역할을 하나 내부 구조가 +연산이 느릴 수 있음(배열을 loop돌기 때문)
print(t2)

s = "one:two:three:four:five"
print(s.rsplit(":", 2))
print(s.rsplit(":", 1))

lines = """1st line
2nd line
3rd line
4th line
"""
print("-----------lines-----------------")
print(lines.splitlines())

tempLine = lines.splitlines()
print(tempLine[1])

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('abcd'.isdigit())
print('1234'.isalpha())

print('abcd'.islower())
print('ABCD'.isupper())

print(''.isspace())
print('\n\n'.isspace())
print('                '.isspace())

# 0로 채우기 - '20'을 가진 string 5자리를 만들고, 나머지를 0으로 채움
print('20'.zfill(5))

# format
f = 'name:{0}, age{1}'
print(f.format(name, age))
print('name:{1}, age{0}'.format(age, name))

d = {'name': '마이콜', 'age':20}
print('name:{name}, age:{age}'.format_map(d))