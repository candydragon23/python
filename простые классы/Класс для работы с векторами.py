import math
class Vector:

    def funclen(self, x, y):
        return (x ** 2 + y ** 2) ** 0.5

    def len(self):
        print('Введите координаты x, y вектора')
        l = [_ for _ in input().split()]
        try:
            x, y = map(int, l)
        except ValueError:
            print('Неправильные входные данные')
            exit(-1)
        print('Длина вектора равна:')
        return (x ** 2 + y ** 2) ** 0.5

    def deg(self):
        print('Введите координаты x, y вектора')
        l = [_ for _ in input().split()]
        try:
            x, y = map(int, l)
        except ValueError:
            print('Неправильные входные данные')
            exit(-1)
        print('Угол наклона равен:')
        if x == 0:
            return 90
        else:
            cos = x / self.funclen(x, y)
            if x > 0:
                return (math.acos(cos) * 180) / math.pi
            else:
                return 360 - (math.acos(cos) * 180) / math.pi


    def sum(self):
        print('Введите координаты 2-х векторов x1, y1, x2, y2')
        l = [_ for _ in input().split()]
        try:
            x1, y1, x2, y2 = map(int, l)
        except ValueError:
            print('Неправильные входные данные')
            exit(-1)
        newvec = [x1 + x2, y1 + y2]
        print('Сумма векторов равна:')
        return newvec

    def sub(self):
        print('Введите координаты 2-х векторов x1, y1, x2, y2')
        l = [_ for _ in input().split()]
        try:
            x1, y1, x2, y2 = map(int, l)
        except ValueError:
            print('Неправильные входные данные')
            exit(-1)
        newvec = [x1 - x2, y1 - y2]
        print('Разность векторов равна:')
        return newvec

    def mult(self):
        print('Введите координаты 2-х векторов x1, y1, x2, y2')
        l = [_ for _ in input().split()]
        try:
            x1, y1, x2, y2 = map(int, l)
        except ValueError:
            print('Неправильные входные данные')
            exit(-1)
        len1 = self.funclen(x1, y1)
        len2 = self.funclen(x2, y2)
        print('Скалярное произведение векторов равно:')
        return len1 * len2

print('Введите желаемую функцию')
print('Список функций: len, deg, sum, sub, mult')
func = input()
vec = Vector()
if func == 'len': print(vec.len())
elif func == 'deg': print(vec.deg(), ' градусов')
elif func == 'sum': print(*vec.sum())
elif func == 'sub': print(*vec.sub())
elif func == 'mult': print(vec.mult())
else: print('Такой функции не существует')
