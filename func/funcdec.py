# coding: utf-8
# 装饰器语法糖 @dec


def dec(func):
    print('call dec')

    def in_dec(*args):
        print('in dec args=', args)
        if len(args) == 0:
            return 0
        for val in args:
            if not isinstance(val, int):
                return 0
        return func(*args)

    return in_dec


@dec
def my_sum(*args):
    print('in my_sum')
    return sum(args)


print(my_sum(1, 2, 3, 4, 5))
