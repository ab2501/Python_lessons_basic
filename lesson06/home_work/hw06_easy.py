# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


class Side:
    @staticmethod
    def width(A, B):
        return round(sqrt(sum(tuple(map(lambda a, b: (b - a)**2, A, B)))), 2)


class Triangle(Side):
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C

    def sides(self):
        return {'AB': self.width(self._A, self._B),
                'BC': self.width(self._B, self._C),
                'CA': self.width(self._C, self._A)
                }

    def perimeter(self):
        return round(self.sides()['AB'] +
                     self.sides()['BC'] +
                     self.sides()['CA'], 2)

    def area(self):
        return round((lambda p, a, b, c:
                      sqrt(p*(p - a)*(p - b)*(p - c)))
                      (self.perimeter() / 2,
                       self.sides()['AB'],
                       self.sides()['BC'],
                       self.sides()['CA']), 2)

A1, A2, A3 = (7, -13), (-9, 9), (12, -11)

ABC = Triangle(A1, A2, A3)

print('В треугольнике со сторонами:')
print(' см\n'.join([str(side) for side in ABC.sides().values()]) + ' cм')
print('Площадь: {} кв.см'.format(ABC.area()))
print('Периметр: {} см'.format(ABC.perimeter()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapeze:
    def __init__(self, a, b, c, d):

        try:
            self.AB = round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2), 2)
            self.CD = round(math.sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2), 2)
            self.DA = round(math.sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2), 2)
        except TypeError:
            print('Параметры заданы неправильно')

    def isosceles(self):
        return self.AB == self.CD

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA, 2)

    def area(self):
        if self.isosceles():
            h = math.sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            return round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.perimeter() / 2
            return round((self.BC + self.DA)/abs(self.DA - self.BC) *
                         math.sqrt((p-self.DA)*(p-self.BC) *
                                   (p-self.DA-self.AB) *
                                   (p-self.DA-self.CD)), 2)


trap = Trapeze((-7, 4), (-5, 6), (6, 6), (8, 5))

print('Трапеция с основаниями DA и BC\nявляется равнобокой: {0}\n'
      'с Площадью {1} кв.см и Периметром {2} '
      'см'.format(trap.isosceles(), trap.area(), trap.perimeter()))