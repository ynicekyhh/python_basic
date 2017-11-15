# 다음과 같은 테스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>"""

# 내 풀이
# lines = s.splitlines()
#
#
# for line in lines:
#     if line.find("<h4>") > 0:
#         line = line.replace("<h4>", '')
#         line = line.replace('</h4>', '')
#         print(line)
#     elif line.find("<a") > 0:
#         line = line.replace(line[line.find('<a href'):line.find("'>")+2], '')
#         line = line.replace('</a>', '')
#         print(line)
#     else:
#         print(line[:line.find("<")])

# 강사님 풀이
# idxbegin = 0
#
# while True:
#     idxbegin = s.find('<', idxbegin)
#     if idxbegin == -1:
#         break
#     idxend = s.find('>')
#     if idxend != -1:
#         s = s[:idxbegin] + s[idxend+1:]
#     else:
#         idxend += 1
#
# print(s)

# 웅섭이 풀이
flag = True
for c in s:
    if c == '<':
        flag = False
        continue
    elif c == '>':
        flag = True
        continue

    if flag == True:
        print(c, end='')
