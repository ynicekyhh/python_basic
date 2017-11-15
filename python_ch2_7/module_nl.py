# import한 모듈 이름 리스팅


import mod_a
import mod_b
from mymod import add
import mymod2
from math import sin
import sys

print(add.__module__)
print(sin.__module__)

for key in sys.modules.keys():
    print(key)

