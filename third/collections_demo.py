# coding: utf-8

from collections import namedtuple
from collections import deque
from collections import OrderedDict
from collections import Counter

Point = namedtuple('point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 如果要保持Key的顺序，可以用OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys())


# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] += 1

print(c)
