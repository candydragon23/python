#Поля данных класса не обязательно задавать заранее. Их можно создавать на ходу
class Circle:
    pass
my_circle = Circle()
my_circle.radius = 5
print(my_circle.radius * 2)
#Методы класса
class Legs:
    count = 4
    def getlegs(self):
        return self.count
charlie = Legs()
print(charlie.count)
print(charlie.getlegs())
#В первом аргументе любого метода передается экземпляр, для которого он вызывается; по действующим правилам он называется self
class Circle3:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius
#Инициализация полей класса __init__
#Эта функция выполняется при каждом создании экземпляра класса
#Новый экземпляр передается а первом аргументе self
class Circle2:
    def __init__(self):
        self.radius = 1
my_circle = Circle2()
print(2 * my_circle.radius)
my_circle.radius = 5
print(2 * my_circle.radius)
#Ограничение на свойства __slots__
#В качестве значения slots может быть указана строка, объект поддерживающий итерирование, или последовательность строк с именами атрибутов
class ComplexNumber:
    __slots__ = ('r', 'i')
    def __init__(self,x,y):
        self.r = x
        self.i = y
a = ComplexNumber(3, 3)
print(a.r)
print(a.i)
#Деструктор класса (почти не используется в питоне)
class A:
    def __init__(self):
        self.x = 10
    def __del__(self):
        print("Удаление")
a = A()
print(a.x)
del a