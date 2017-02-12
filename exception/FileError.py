# coding: utf-8

# 自定义exception


class CustomError(IOError):
    def __init__(self, info):
        Exception.__init__(self)
        self.strerror = info
        print(id(self))

    def __str__(self):
        return "CustomError: %s" % self.strerror


try:
    raise CustomError('Test FileError')
except CustomError as e:
    print(id(e))
    print(e)
