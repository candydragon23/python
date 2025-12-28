class Product:
    def __init__(self, name, cost, weight):
        self.__name = name
        self.__cost = cost
        self.__weight = weight

    @property
    def getName(self):
        return self.__name

    @property
    def getCost(self):
        return self.__cost

    @property
    def getWeight(self):
        return self.__weight

class Buy(Product):
    def __init__(self, name, cost, weight, amount):
        super().__init__(name, cost, weight)
        self.__amount = amount

    cost = Product.getCost
    @property
    def costTotal(self):
        return cost * self.__amount

    weight = Product.getWeight
    @property
    def weightTotal(self):
        return weight * self.__amount

class Check(Buy):
    def info(self):
        print(f'Имя товара: {self.getName}')
        print(f'Стоимость товара: {self.getCost}')
        print(f'Вес товара: {self.getWeight}')
        print(f'Общая стоимость товаров: {self.costTotal}')
        print(f'Общий вес товаров: {self.weightTotal}')

print('Введите название продукта, его цену, вес и количество (имя, цена, вес, количество)')
l = [_ for _ in input().split()]
if len(l) != 4:
    print('Неправильный ввод')
    exit(-1)
name = l[0]
try: cost, weight, amount = map(float, (l[_] for _ in range(1, 4)))
except ValueError:
    print('Неправильный ввод')
    exit(-1)
amount = int(amount)
check = Check(name, cost, weight, amount)
check.info()