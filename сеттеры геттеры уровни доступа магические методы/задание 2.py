class User:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, new_name):
        if not new_name.isalpha():
            print('Некорректное имя')
            quit('ValueError')
        self.__name = new_name

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        try: new_age = int(new_age)
        except ValueError:
            print('Некорректный возраст')
            quit('ValueError')
        if new_age < 0 or new_age > 110:
            print('Некорректный возраст')
            quit('ValueError')
        self._age = new_age

func = ' '
print('Введите имя пользователя')
name = input()
if not name.isalpha():
    print('Некорректное имя')
    quit('ValueError')
print('Введите возраст пользователя')
try:
    age = int(input())
    if age < 0 or age > 110:
        print('Некорректный возраст')
        quit('ValueError')
except ValueError:
    print('Некорректный возраст')
    quit('ValueError')
user = User(name, age)
while func != '':
    print('Выберите действие')
    print('Доступные действия: getname, setname, getage, setage')
    func = input()
    if func == 'getname':
        name = user.get_name
        print(name)
    elif func == 'setname':
        print('Введите новое имя')
        new_name = input()
        user.set_name = new_name
    elif func == 'getage':
        age = user.get_age
        print(age)
    elif func == 'setage':
        print('Введите новый возраст')
        new_age = input()
        user.set_age = new_age
    elif func != '':
        print('Такой функции не существует')