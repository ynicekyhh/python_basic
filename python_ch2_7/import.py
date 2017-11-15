# 다양한 import 방법

# import math
# print(math.pi/6, math.cos(math.pi/3))

# from ~ import (특정 객체들을 import하여 바로 사용할 수 있음)
# 하지만 내가 작업중인 다른 변수들과 충돌날 수 있다. (덮어버릴 수 있음)
# 따라서 편한 방법이긴 하지만 여러 lib를 사용할 경우 추천하지 않음
# from math import pi, cos
# print(pi/6, cos(pi/3))


# math에 있는 모든 함수, 변수 객체들을 다 가져옴
# from math import *
# import 시 긴 이름일 경우 arias를 줘서 사용할 수 있음
# import mymath as mm
# print(pi/6, mm.pi/3, cos(pi/3), sin(pi/4))


# 아래와 같이 사용하지는 않으나, 가능하다.
# from math import cos as mycos, pi as mypi
# print(mypi/6, mycos(mypi/3))