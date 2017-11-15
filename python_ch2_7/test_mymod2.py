# mymod2에서 mymod를 import하는데, 여기서 또 import를 하면 이미 import가 mymod2에서 일어났기 때문에 캐시에서 가져오니 중복되지 않는다.
import mymod2
import mymod

print(mymod.add(10, 20))
print(mymod2.power(2, 10))
