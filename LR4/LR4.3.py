# -*- coding: utf-8 -*-
# Реализуйте базовый класс Car.
# 1. У класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# 2. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar;
# 3. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля;
# 4. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Машина едет")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула", direction)

    def show_speed(self):
        if (self.speed > 0):
            self.go()
            print("со скоростью", self.speed, "км/ч")
        else:
            self.stop()

class TownCar(Car):
    def show_speed_town_car(self):
        self.show_speed()
        if self.speed > 60:
            print("Внимание!", self.color, self.name, "превысил скорость на ", self.speed - 60, "км/ч")

class SpotCar(Car):
    def show_speed_sport_car (self):
        self.show_speed()

class WorkCar(Car):
    def show_speed_work_car(self):
        self.show_speed()
        if self.speed > 40:
            print("Внимание!", self.color, self.name, "превысил скорость на ", self.speed - 60, "км/ч")

class PoliceCar(Car):
    def show_speed_police_car(self):
        self.show_speed()

town_car = TownCar(20,"Красная", "Toyota", "Нет")
town_car.show_speed_town_car()
print("\n")

work_car = WorkCar(100,"Черный", "Ford", "Нет")
work_car.show_speed_work_car()
print("\n")

police_car = PoliceCar(0,"Белый", "Dodge", "Да")
police_car.show_speed_police_car()
print("\n")