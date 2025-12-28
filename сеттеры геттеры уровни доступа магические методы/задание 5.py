class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.pt = proteins
        self.ft = fats
        self.ch = carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.pt},{self.ft},{self.ch})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.pt + other.pt, self.ft + other.ft, self.ch + other.ch)
        return NotImplemented

    def __mul__(self, n):
        return FoodInfo(self.pt * n, self.ft * n, self.ch * n)

    def __truediv__(self, n):
        return FoodInfo(self.pt / n, self.ft / n, self.ch / n)

    def __floordiv__(self, n):
        return FoodInfo(self.pt // n, self.ft // n, self.ft // n)

func = ' '
print('Введите количество белков, жиров и углеводов в продукте (в граммах)')
l = [int(_) for _ in input().split()]
try: pt, ft, ch = l
except ValueError:
    print('Неправильные входные данные')
    exit(-1)
food = FoodInfo(pt, ft, ch)
while func != '':
    print('Выберите действие')
    print('Список действий: sum, mult, div, fldiv')
    func = input()
    if func == 'sum':
        print('Введите количесто белков, жиров и углеводов во втором продукте (в граммах)')
        l = [int(_) for _ in input().split()]
        try: pt2, ft2, ch2 = l
        except ValueError:
            print('Неправильные входные данные')
            break
        food2 = FoodInfo(pt2, ft2, ch2)
        food += food2
        print(f'Результат суммы: {food.pt} грамм белков, {food.ft} грамм жиров, {food.ch} грамм углеводов')
    elif func == 'mult':
        print('Введите натуральное число n')
        n = int(input())
        if n < 0:
            print('Неправильно задано число n')
            break
        food *= n
        print(f'Результат умножения: {food.pt} грамм белков, {food.ft} грамм жиров, {food.ch} грамм углеводов')
    elif func == 'div':
        print('Введите натуральное число n')
        n = int(input())
        if n < 0:
            print('Неправильно задано число n')
            break
        food /= n
        print(f'Результат деления: {food.pt} грамм белков, {food.ft} грамм жиров, {food.ch} грамм углеводов')
    elif func == 'fldiv':
        print('Введите натуральное число n')
        n = int(input())
        if n < 0:
            print('Неправильно задано число n')
            break
        food //= n
        print(f'Результат деления нацело: {food.pt} грамм белков, {food.ft} грамм жиров, {food.ch} грамм углеводов')
    elif func != '': print('Такого действия нет')