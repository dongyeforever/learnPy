# encoding: utf-8


class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

    def __str__(self):
        return 'Student object (brith=%s)' % self._birth

    __repr__ = __str__

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己


s = Student()
s.birth = 20
print(s.birth)
print(s.__str__())
# print(s.__repr__)
