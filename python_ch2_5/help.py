# help 함수
help(print)


def plus(a, b):
    """
    __doc__을 사용하지 않는 경우 이런식으로 주석을 이용해 document역할을 할 수 있음
    :param a:
    :param b:
    :return:
    """
    return a+b


# plus.__doc__ = 'return the sum of parameter a, b'
help(plus)
print(plus.__doc__)     # 위의 help와 동일함

