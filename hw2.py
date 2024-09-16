#2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
#Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'The amount of fabric is: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Smth vary abstract'


class Coat(Clothes):
    def consumption(self):
        return f'for coat needs: {self.param / 6.5 + 0.5 :.2f} '

    def abstract(self):
        return 'Smth vary abstract second'


class Costume(Clothes):
    def consumption(self):
        return f'for suit needs: {2 * self.param + 0.3 :.2f} '

    def abstract(self):
        pass


coat = Coat(50)
costume = Costume(1.80)
print(coat.consumption())
print(costume.consumption())
print(coat.abstract())
