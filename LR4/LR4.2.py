# -*- coding: utf-8 -*-
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
# переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение; создать экземпляры классов и проверить, что
# выведет описанный метод для каждого экземпляра.
class Stationery:
     title = 'Канц.товары'
     def __init__(self):
         self.name = 'нет'
     def draw(self):
         print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        self.name = 'ручка'
    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def __init__(self):
        self.name = 'карандаш'
    def draw(self):
        print('Запуск отрисовки')

class Handle(Stationery):
    def __init__(self):
        self.name = 'маркер'
    def draw(self):
        print('Запуск отрисовки')

a=Stationery()
b=Pen()
c=Pencil()
d=Handle()
print(f'{a.title}-{a.name}, {b.name}, {c.name}, {d.name}')

a.draw()
b.draw()
c.draw()
d.draw()

