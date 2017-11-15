# 다음 문자열을 모든 대문자를 소문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 각 단어를 순서대로 출력하세요.

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

# 문자열 처리를 한 후에 set?

# l = ['we', 'to', 'encourage', 'to', 'group']
# list를 set으로 변환하면 중복을 제거해준다.
# list, tuple, set은 서로 형 변환이 자유롭다.
# s = set(l)
# l = list(s)
#
# print(s)

s = s.replace(',', '')
s = s.replace('.', '')
s = s.replace('\n', '')
s = s.upper()
s = s.split(' ')
s = set(s)
s = sorted(s, key=str)

for str in s:
    print('{0}:{1}'.format(str, str.count(str)))

