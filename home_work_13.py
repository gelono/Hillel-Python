# 1. Доопрацюйте всі реревірки на типи даних (x, y в Point, begin, end в Line, etc) - зробіть перевірки за допомогою
# property або класса-дескриптора.
# 2. Доопрацюйте класс Triangle з попередньої домашки наступним чином:
#    a. обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
#    b. перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3

from abc import ABC, abstractmethod
from math import sqrt


class Point:
    _x = None
    _y = None

    def __init__(self, val_x, val_y):
        self.x = val_x
        self.y = val_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._y = value


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        pass

    @abstractmethod
    def length(self):
        pass


class Line(Figure):
    _begin = None
    _end = None

    def __init__(self, begin_value, end_value):
        self.begin = begin_value
        self.end = end_value

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def length(self):
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res


class Triangle:
    _point_a = None
    _point_b = None
    _point_c = None

    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    @property
    def point_a(self):
        return self._point_a

    @point_a.setter
    def point_a(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point_a = value

    @property
    def point_b(self):
        return self._point_b

    @point_b.setter
    def point_b(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point_b = value

    @property
    def point_c(self):
        return self._point_c

    @point_c.setter
    def point_c(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._point_c = value

    def triangle_area(self):
        line_ab = Line(self.point_a, self.point_b)  # triangle line initialization
        line_bc = Line(self.point_b, self.point_c)  # triangle line initialization
        line_ac = Line(self.point_a, self.point_c)  # triangle line initialization

        length_ab = line_ab.length()
        length_bc = line_bc.length()
        length_ac = line_ac.length()

        half_perim = (length_ab + length_bc + length_ac) / 2
        area = sqrt(half_perim * (half_perim - length_ab) * (half_perim - length_bc) * (half_perim - length_ac))

        return area

    def __eq__(self, other):
        return self.triangle_area() == other.triangle_area()

    def __ne__(self, other):
        return self.triangle_area() != other.triangle_area()

    def __lt__(self, other):
        return self.triangle_area() < other.triangle_area()

    def __gt__(self, other):
        return self.triangle_area() > other.triangle_area()

    def __ge__(self, other):
        return self.triangle_area() >= other.triangle_area()

    def __le__(self, other):
        return self.triangle_area() <= other.triangle_area()

    def __str__(self):
        string = f'({self.point_a.x},{self.point_a.y} -- {self.point_b.x},{self.point_b.y} -- {self.point_c.x},{self.point_c.y})'
        return string


point_a1 = Point(1, 20)
point_b1 = Point(10, 4)
point_c1 = Point(5, 60)

point_a2 = Point(5, 25)
point_b2 = Point(15, 10)
point_c2 = Point(50, 65)

triangle_1 = Triangle(point_a1, point_b1, point_c1)
triangle_2 = Triangle(point_a2, point_b2, point_c2)

print(str(triangle_1))
print(str(triangle_2))
print(f'area1 = {triangle_1.triangle_area()}')
print(f'area2 = {triangle_2.triangle_area()}')
print(triangle_1 == triangle_2)
print(triangle_1 != triangle_2)
print(triangle_1 > triangle_2)
print(triangle_1 < triangle_2)
print(triangle_1 <= triangle_2)
print(triangle_1 >= triangle_2)