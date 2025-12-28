import math
import random

class ThreeDShapes:
    pass

class Paral(ThreeDShapes):
    def __init__(self, length, width, height):
        self.a = length
        self.b = width
        self.c = height

    def areaSize(self, a, b):
        return a * b

    @property
    def fullAreaSize(self):
        return 2 * (self.areaSize(self.a, self.b) + self.areaSize(self.a, self.c) + self.areaSize(self.b, self.c))

    @property
    def volume(self):
        return self.a * self.b * self.c

class Cube(Paral):
    def __init__(self, length):
        super().__init__(length, length, length)

    @property
    def fullAreaSize(self):
        return 6 * self.areaSize(self.a, self.a)

class Ellips(Paral):
    @property
    def fullAreaSize(self):
        p = 1.6075
        return 4 * math.pi * ((self.a ** p * self.b ** p + self.a ** p * self.c ** p + self.b ** p * self.c ** p) / 3) ** (1 / p)

    @property
    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c

class Sphere(ThreeDShapes):
    def __init__(self, radius):
        self.r = radius

    def areaSize(self):
        return math.pi * self.r ** 2

    @property
    def fullAreaSize(self):
        return 4 * self.areaSize()

    @property
    def volume(self):
        return  (4 / 3) * self.areaSize() * self.r

class Cylinder(Sphere):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.h = height

    def sideAreaSize(self):
        return 2 * math.pi * self.r * self.h

    @property
    def fullAreaSize(self):
        return 2 * self.areaSize() + self.sideAreaSize()

    @property
    def volume(self):
        return self.areaSize() * self.h

def rand():
    return round(random.uniform(1, 100), 1)

def volumeCheck(volumes): #Поиск объема вмещающего все остальные объемы
    info = []
    maxVolume = 0
    index = 0
    for volume in volumes:
        if volume > maxVolume:
            maxVolume = volume
            maxindex = index
        index += 1
    volumeSum = sum(volumes) - maxVolume
    if maxVolume >= volumeSum:
        if maxindex == 0: info.append('Параллелепипед')
        elif maxindex == 1: info.append('Куб')
        elif maxindex == 2: info.append('Шар')
        elif maxindex == 3: info.append('Цилиндр')
        elif maxindex == 4: info.append('Эллипсоид')
        info.append(maxVolume)
        return info
    else:
        info = [0, 0]
        return info

def checkNumbers(l):
    try: l = list(map(float, l))
    except ValueError:
        print('Неправильный ввод')
        exit(-1)
    return l

def checkSize(l, size):
    if len(l) != size:
        print('Введено неправильное количество значений')
        exit(-1)
    else:
        return l

print('Введите тип ввода (rand (рандомная генерация), inpt (ручной ввод)')
type = input()
if type == 'rand':
    paral = Paral(rand(), rand(), rand())
    cube = Cube(rand())
    ellips = Ellips(rand(), rand(), rand())
    sphere = Sphere(rand())
    cylinder = Cylinder(rand(), rand())
elif type == 'inpt':
    print('Введите значения для длины, ширины и высоты параллелепипеда')
    l = checkSize(checkNumbers([_ for _ in input().split()]), 3)
    paral = Paral(*l)
    print('Введите значение для длины ребра куба')
    l = checkSize(checkNumbers([_ for _ in input().split()]), 1)
    cube = Cube(*l)
    print('Введите значения 3-х осей эллипсоида')
    l = checkSize(checkNumbers([_ for _ in input().split()]), 3)
    ellips = Ellips(*l)
    print('Введите значение радиуса шара')
    l = checkSize(checkNumbers([_ for _ in input().split()]), 1)
    sphere = Sphere(*l)
    print('Введите радиус основания цилиндра и его высоту')
    l = checkSize(checkNumbers([_ for _ in input().split()]), 2)
    cylinder = Cylinder(*l)
else:
    print('Такого типа не существует')
    exit(-1)
print(f'Площадь полной поверхности параллелепипеда: {paral.fullAreaSize}')
print(f'Объем параллелепипеда: {paral.volume}')
print(f'Площадь полной поверхности куба: {cube.fullAreaSize}')
print(f'Объем куба: {cube.volume}')
print(f'Площадь полной поверхности эллипсоида: {ellips.fullAreaSize}')
print(f'Объем эллипсоида: {ellips.volume}')
print(f'Площадь полной поверхности шара: {sphere.fullAreaSize}')
print(f'Объем шара: {sphere.volume}')
print(f'Площадь полной поверхности цилиндра: {cylinder.fullAreaSize}')
print(f'Объем цилиндра: {cylinder.volume}')
volumes = [paral.volume, cube.volume, sphere.volume, cylinder.volume, ellips.volume]
maxVolumeInfo = volumeCheck(volumes)
if maxVolumeInfo[1] != 0:
    print(f'{maxVolumeInfo[0]} вмещает все остальные объемы')
    print(f'Его объем равен: {maxVolumeInfo[1]}')
else:
    print('Объема вмещающего все объемы не найдено')
