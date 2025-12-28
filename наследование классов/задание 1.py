class Counter:
    def __init__(self, start):
        self.value = start

    def inc(self, amount):
        if amount != -1:
            self.value += amount
            print(f'Текущее значение счетчика: {self.value}')

    def dec(self, amount):
        if amount != -1:
            if self.value - amount < 0:
                self.value = 0
            else:
                self.value -= amount
            print(f'Текущее значение счетчика: {self.value}')

class NonDecCounter(Counter):

    def dec(self, amount):
        pass

class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__(start)
        self.limit = limit

    def inc(self, amount):
        if amount != -1:
            if self.value + amount > self.limit:
                print('Значение превышает счетчик')
            else:
                self.value += amount
                print(f'Текущее значение счетчика: {self.value}')

def tryNumber(num):
    try:
        num = int(num)
    except ValueError:
        print('Неправильный ввод')
        return -1
    if num < 0:
        print('Число должно быть положительным')
        return -1
    return num

def checkType(type):
    if type == 'c':
        counter = Counter(start)
    elif type == 'ndc':
        counter = NonDecCounter(start)
    else:
        print('Введите границу счетчика (натуральное число) (по умолчанию 10)')
        limit = input()
        if limit == '':
            limit = 10
        else:
            limit = tryNumber(limit)
        if limit < start:
            print('Предел меньше начального значения')
            exit(-1)
        else:
            counter = LimitedCounter(limit)
    return counter

print('Введите тип счетчика')
print('Доступные типы: c, ndc, lc')
type = input()
if type != 'c' and type != 'ndc' and type != 'lc':
    print('Неправильный ввод')
    exit(-1)
print('Введите начальное значение счетчика (натуральное число) (по умолчанию 0)')
start = input()
if start == '':
    start = 0
    counter = checkType(type)
else:
    start = tryNumber(start)
    counter = checkType(type)
func = ' '
while func != '':
    print('Выберите действие')
    print('Список действий: inc, dec (ведите пустую строку для завершения работы)')
    func = input()
    if func == 'inc':
        print('Введите число на которое нужно увеличить счетчик')
        amount = input()
        if amount == '':
            amount = 1
        else:
            amount = tryNumber(amount)
        counter.inc(amount)
    elif func == 'dec':
        print('Введите число на которое нужно уменьшить счетчик')
        amount = input()
        if amount == '':
            amount = 1
        else:
            amount = tryNumber(amount)
        counter.dec(amount)
    elif func != '': print('Такой функции не существует')