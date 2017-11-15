import sys

# print() 연습
print(1)
print('hello', 'world', sep='   ', end='\n')
print('hello python')

x = 0.2
a = 'hello'

print(x, a)
# '+' 연산자는 오버로드를 해서 구현된 애들만 사용 가능한데, 내장객체들은 대부분 오버로드로 구현시켜 놨음, print 함수도 마찬가지임
# print에서 '+'는 Java와 달리 문자 + 숫자를 지원하지 않으니 아래처럼 형을 통일시켜줘야함
print(str(x) + ":" + a)
# 아래와 같은 방법으로는 타입을 통일시키지 않아도 가능
print(x, a, sep=":")
print('{0}:{1}'.format(x, a))

# 기본적으로 print() 호출은 아래와 같다
print(sep=' ', end='\n')

# file 파라미터
print('Hello World', file=sys.stdout)
print('Error: Hello World', file=sys.stderr)

# file로 출력 - mode는 기본이 txt니까 'wt'같이 할 필요없이 't'를 생략했다.
f = open('hello.txt', 'w')
print('Hello World', file=f)

# 참고
sys.stdout.write('hello world')