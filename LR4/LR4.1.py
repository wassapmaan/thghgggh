# Класс Square
# Создайте класс Square. В нём пропишите 3 (метода) функции. Первый метод:
# нахождение периметра квадрата. Второй метод: нахождение площади
# квадрата. Третий метод: нахождение диагонали квадрата.

class Square:
    def __init__(self, length):
        self.length = length
    def find_perimetr(self):
        return 4*self.length
    def find_square(self):
        return self.length * self.length
    def find_diagonal(self):
        return 2*self.length*self.length

a=Square(5)
print(a.find_square())
print(a.find_diagonal())
print(a.find_perimetr())