# lamda 함수


def blahblah(x):
    return x**2


for i in range(10):
    print("{0}:{1}".format(i, blahblah(i)), end=' ')
else:
    print()

for i in range(10):
    print("{0}:{1}".format(i, (lambda x:x**2)(i)), end=' ')
else:
    print()

strings = ['a', 'a', 'a', 'foo', 'card', 'bar', 'abab', 'aaaa', 'abab', 'foo']
strings.sort(key=lambda x: len(x), reverse=True)
print(strings)


strings = sorted(strings, key=lambda x: strings.count(x))
# 아래의 방법으로 하면 strings가 global이 아니라 내부에서 또 정의되어 모두 0이 되는듯 위의 방법으로 하자
# def k(x, l):
#     print('{0}:{1}'.format(x, l))
#     return l.count(x)

# strings.sort(key=lambda x: k(x, strings), reverse=False)

print(strings)