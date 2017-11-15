# 동적 import를 위한 __import__ 사용
# 일반적으로 잘 사용하지 않으나, 어떤 프로그램 실행 도중에 다운로드 후 import를 해야하는 경우 dynamic import를 사용함
#
mm = __import__('mymod')

print(mm.add(10, 20))
