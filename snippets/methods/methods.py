from __future__ import division
from math import sqrt


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt(self.x * other.x + self.y * other.y)


p1 = Point(1, 3)
p2 = Point(2, 4)
print p1.distance(p2)  # 3.74165738677
print p2.distance(p1)  # 3.74165738677
