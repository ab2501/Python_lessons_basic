#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      a.butarev
#
# Created:     09.11.2018
# Copyright:   (c) a.butarev 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Лото-классы
import random
import config


class CardGenerator:

    def __init__(self, title='Карта',  N=config.N, line=config.line,
                 n=config.n, empty=config.empty, char=config.char):

        try:
            self._title = title
            self._N = list(range(1, N+1))
            self._line = line
            self._n = n
            self._empty = empty
            self._char = char
            self._lines = list(self)  # массив строк карты
        except TypeError:
            print('Неверно заданы параметры конфигурации')

    def __iter__(self):
        return self

    def __next__(self):
        if self._line:
            line = []
            try:
                while len(set(line)) != self._n:
                    line = list(map(lambda x: ' ' + str(x) if
                                    len(str(x)) == 1 else str(x),
                                    sorted([random.choice(self._N) for
                                            _ in range(self._n)])))

                self._N = list(set(self._N) - set([int(x) for x in line]))

                while line.count(self._char) != self._empty:
                    rand_num = random.choice(line)
                    line = list(map(lambda x: x.replace(rand_num, self._char),
                                line))
            except AttributeError:
                print('Ошибка при генерации строки карты')

            self._line -= 1
            return line
        else:
            raise StopIteration

    def __str__(self):
        return '{:-^26}\n{}\n{:-^26}' \
               ''.format(self._title,
                         '\n'.join(list(map(
                                   lambda x: ' '.join(x), self._lines))), '-')

    def is_include(self, num):

        return not len([line for line in self._lines if
                       (lambda x: ' ' + str(x)
                        if len(str(x)) == 1 else str(x))(num) in line]) is 0

    def cross_out(self, num):

        self._lines = [list(map(lambda x: x.replace(
                     (lambda x: ' ' + str(x) if len(str(x)) == 1 else
                      str(x))(num), ' -'), line)) for line in self._lines]
        return self

    def is_win(self):

        return len(list(filter(lambda x: x.count(' -') != self._n-self._empty,
                               self._lines))) is 0


class BarrelGenerator:

    def __init__(self, N=config.N):

        try:
            self._N = list(range(1, N+1))
            self._barrel = None
        except TypeError:
            print('Не удаётся определить число бочонков в мешке')

    def __iter__(self):
        return self

    def __str__(self):
        return str(next(self))

    def __next__(self):
        if len(self._N):
            self._barrel = random.choice(self._N)
            self._N = list(filter(lambda x: x != self._barrel, self._N))
            return self._barrel
        else:
            raise StopIteration

    @property
    def length(self):

        return len(self._N)

    @property
    def current_number(self):

        return self._barrel