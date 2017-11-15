# class Point
# class 내에 변수를 만들지 않는데, 그 이유는 클래스 인스턴스가 class Point와 다른 공간을 사용하기 때문
# p = Point()라고 할 때, p가 가지는 공간과 class Point의 공간이 다름.
# 따라서 Point안에 x라는 변수가 있을 때 p.x를 하면 파이썬 룰에 따라 p에 없으면 Point에서 x를 찾으나
# 실제로 p안에 x가 없어 여러 개의 Point 인스턴스가 생성될 시 문제될 수 있음

# class instance method에 parameter로 self가 들어오면 self는 클래스 인스턴스변수를 지칭한다.
# static method는 @staticmethod 어노테이션을 붙여줘야한다.
# class method는 cls를 파라미터로 입력하여 class안의 변수를 사용하기 위함으로 사용된다.

class Point:
    count_of_instance = 0

    # 생성자
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.count_of_instance += 1

    def __del__(self):
        Point.count_of_instance -= 1

    def __str__(self):
        return "Point(x={0}, y={1})".format(self.x, self.y)

    def __repr__(self):
        return "\"Point({0}, {1})\"".format(self.x, self.y)

    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def show(self):
        print('{%d}, {%d}점을 그렸소.' % (self.x, self.y))

    @staticmethod
    def static_method():
        print('static_method() called')

    @classmethod
    def class_method(cls):
        print('인스턴스 개수: {0}'.format(cls.count_of_instance))
        # print('class method() called')