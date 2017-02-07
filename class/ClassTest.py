# encoding: utf-8


class Programer(object):
    hoby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @property
    def get_weight(self):
        return self.__weight

    @classmethod
    def get_hoby(cls):
        return cls.hoby

    def self_introduction(self):
        print('My name is %s, I am %s years old\n' % (self.name, self._age))

    def __getattribute__(self, name):
        return super(Programer, self).__getattribute__(name)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class BackgroundProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackgroundProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My name is %s, My favorite language is %s\n' % (self.name, self.language))


def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    programer = BackgroundProgramer('Albert', 25, 60, 'Python')
    print(dir(programer))
    print(programer.__dict__)
    print(type(programer))
    print(isinstance(programer, Programer))
    print(issubclass(BackgroundProgramer, Programer))
    introduce(programer)
    print(programer.name)
    programer.__setattr__('name', 'zhangsan')
    print(programer.name)

