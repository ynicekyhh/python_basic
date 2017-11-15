from point import Point
from rect import Rect


def test_bound_instance_method():
    p = Point()
    p.set_x(10)
    p.set_y(20)
    print(p.get_x(), p.get_y())
    p.show()
    print(p.count_of_instance)


def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    print(Point.get_x(p), Point.get_y(p))


def test_other_method():
    Point.static_method()
    Point.class_method()


def test_constructor():
    p1 = Point()
    Point.class_method()
    p2 = Point(11, 11)
    Point.class_method()
    p2.class_method()
    p2.class_method()
    p1.class_method()

    p1.show()

    del p1
    Point.class_method()
    p2.show()


def test_to_string():
    p = Point()
    print(p)
    print(repr(p))

    p2 = eval(repr(p))
    print(p2)


def test_operator_overloading():
    p1 = Point(100, 200)
    p2 = Point(50, 50)
    p3 = p1 + p2
    p4 = p1 - p2

    print(p3)
    print(p4)

    p3 += Point(-10, -10)
    p4 -= Point(-10, -10)
    print(p3)
    print(p4)

    # print(Rect(10, 20) == Rect(20, 10))
    # print(Rect(10, 10) > Rect(10, 5))
    # print(Rect(10, 20) < Rect(20, 10))


def main():
    print('\n------ test_bound_instance_method()')
    test_bound_instance_method()
    print('\n------ test_unbound_class_method()')
    test_unbound_class_method()
    print('\n------ test_other_method()')
    test_other_method()
    print('\n------ test_constructor()')
    test_constructor()
    print('\n------ test_to_string()')
    test_to_string()
    print('\n------ test_operator_overloading()')
    test_operator_overloading()

# paint.py가 top level로 실행되면 main()을 실행하라
if __name__ == '__main__':
    main()
