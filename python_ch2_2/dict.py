# 생성
d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d))

# 인덱싱 대신 키 객체로 검색
print(d['basketball'])

# 없는 키 객체면 당연히 에러
# print(d['volleyball'])

# mutable
d['volleyball'] = 6
print(d)

# 길이
print(len(d))

# 확인
print('soccer' in d)
print('volleyball' not in d)

# 다양한 사전 생성
d = dict()
print(d)
d = dict(one=1, two=2)  # 이런 방식의 dict함수 호출로 생성할 수도 있음!!
print(d)

# 튜플을 저장하고 있는 리스트를 아래처럼 넣으면 dictionary로 변환해줌!
d = dict([('three', 3), ('four', 4)])
print(d)

# 사전 키는 변경 불가능한 타입의 객체
d = {}  # set의 생성 또한 {}로 생성하니 명확함을 위해 오류 발생
d[True] = 'True'
d[10] = 'ten'
d['twenty'] = '20'
d[(1, 2, 3)] = '6'
# 아래는 [1, 2, 3]이 list 자료형으로 변경 가능하니 에러발생!, (1, 2, 3)은 tuple 자료형으로 변경 불가능하니 가능
# d[[1, 2, 3]] = '6'
print(d)

# 메서드
# python에 dict_keys라는 자료형을 추가하여 dictionary의 key들만 모아 저장하는 객체이다.
# 마찬가지로 아래의 values나 items도 keys와 같다.
keys = d.keys();
print(keys, type(keys))

for key in keys:
    print('{0}:{1}'.format(key, d[key]))

values = d.values()
print(values, type(values))

items = d.items()
print(items, type(items))
for item in items:
    print('{0}:{1}'.format(item[0], item[1]))
for key, value in items:
    print('{0}:{1}'.format(key, value))

# 값 가져오기
d = {'둘리': '010-1111-1111', '마이콜': '010-2222-2222'}
print(d['둘리'])
print(d.get('둘리'))
# 없는 경우 None 대신에 디폴트값 세팅
print(d.get('도우넛'))

# 없는 경우에는 데이터를 넣고 가져온다.
print(d.setdefault('둘리', '000-0000-0000'))  # '둘리'는 기존에 있으니 안됨
print(d)
print(d.setdefault('도우넛', '000-0000-0000'))
print(d.get('도우넛', '000-0000-0000'))    # setdefault와 동일. get일 때는 key값이 없으면 만들고 value를 넣어줌
print(d)

# 삭제와 동시에 가져오기
print(d.pop('도우넛'))
print(d)

# 튜플형태로 가져오기
n = d.popitem()
print(n)
n = d.popitem()
print(n)
print(d)

# update & clear
# update는 있으면 수정, 없으면 만듦
d.update({'둘리':'010-2222-2222', '길동':'010-3333-3333'})
print(d)
d.clear()
print(d)

# 사전 순회
print('#######사전 순회#######')
d = {'c': 3, 'a': 1, 'b': 2}
for key in d:
    print('{0}:{1}'.format(key, d[key]), end=' ')
else:
    print()

for key, value in d.items():
    print('{0}:{1}'.format(key, value), end=' ')
else:
    print()

