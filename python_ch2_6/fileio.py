# write test

f = open('test.txt', 'w', encoding='utf-8')
writesize = f.write('안녕하세요\n김용호입니다.')
print(writesize)
f.close()

# read test
f = open('test.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

# copy binary file - mode를 안적어주면 default는 'r'이다. 그리고 여기선 binary니까 b를 적어줘야 한다.
f_src = open('python.png', 'rb')
data = f_src.read()
f_src.close()

f_dest = open('python2.png', 'wb')
f_dest.write(data)
f_dest.close()