# for 반복문

a = ['cat', 'dog', 'cow']
for animal in a:
    print(animal)

l = [('둘리', 10), ('마이콜', 20), ('도우넛', 30)]
for t in l:
    print('이름:%s, 나이:%d' % t)

for name, age in l:
    print('이름:{0}, 나이:{1}'.format(name, age))

# for 반복문이 정상적으로 끝나면 else를 실행!
for i in range(10):  # 0 ~ 9까지
    print(i, end=' ')    # end='\n' 이 default 값인데 ''로 변경해주면 print의 라인을 변경하지 않는다.
else:
    print()

s = 0
for i in range(1, 11) :
    s += i
print(s)

# break
for i in range(10):
    if i > 5:
        break
else:
    print('else called')

print('done')

# continue
for i in range(10):
    if i <= 5:
        continue
    print(i, end=' ')
else:
    print()