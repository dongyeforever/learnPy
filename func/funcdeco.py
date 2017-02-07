# encoding= utf-8


def deco(func):
    def in_deco(x, y):
        print('in deco')
        func(x, y)

    print('call deco')
    return in_deco


@deco  # bar = deco(bar)
def bar(x, y):
    print('in bar', x + y)


print(type(bar))
bar(2, 3)
