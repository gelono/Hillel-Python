# 1. Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу
# int або float.
# 2. Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки
# обʼєкти класу Point.
# 3. Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку
# даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для обчислень можна використати
# формулу Герона

from abc import ABC, abstractmethod
from math import sin, sqrt


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self.__dict__[key] = value


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
    begin = None
    end = None

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def length(self):
        res = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return res

    def __setattr__(self, key, value):
        if not isinstance(value, Point):
            raise TypeError
        self.__dict__[key] = value


class Triangle:
    point_a = None
    point_b = None
    point_c = None

    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def __setattr__(self, key, value):
        if not isinstance(value, Point):
            raise TypeError
        self.__dict__[key] = value

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


point_a = Point(1, 20)
point_b = Point(10, 4)
point_c = Point(5, 60)

triangle = Triangle(point_a, point_b, point_c)
print(triangle.triangle_area())