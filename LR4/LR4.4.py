# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса.
class Animal:
     total_animals = 0
     def __init__(self, species, age):
         self.species = species
         self.age = age
         Animal.total_animals +=1
     def description(self):
         print("это", self.species)
         print("ему", self.age, "лет")
     def animal_sound(sound):
         print("оно произносит звук - ", sound)
     def get_total_animals(cls):
         print("всего в зоопарке", cls.total_animals, "животных", end="\n\n")

lion = Animal("лев", 10)
lion.description()
Animal.animal_sound("r-r-r-r-r-r")
Animal.get_total_animals(lion)

monkey = Animal("обезьяна",3)
monkey.description()
Animal.animal_sound("y-y-y-y-y-y-y")
Animal.get_total_animals(monkey)

shark = Animal("змея",2)
shark.description()
Animal.animal_sound("s-s-s-s-s-s-s")
Animal.get_total_animals(shark)
