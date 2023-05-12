from math import sqrt
class Point:
    def __init__(self):
        self.x = float(input())
        self.y = float(input())
        self.z = float(input())


a = Point()
b = Point()
d = sqrt((b.x - a.x)**2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2)
print(d)