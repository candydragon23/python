from functools import total_ordering
@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'Word(\'{self.word}\')'

    def __str__(self):
        self.word = self.word[0].upper() + self.word[1:].lower()
        return self.word

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented

func = ' '
print('Введите первое слово')
word = input()
if not word.isalpha():
    print('Неправильный ввод')
    exit(-1)
print('Введите второе слово')
word2 = input()
if not word2.isalpha():
    print('Неправильный ввод')
    exit(-1)
w1 = Word(word)
w2 = Word(word2)
while func != '':
    print('Выберите операцию')
    print('Список операций: eq, ne, lt, gt, le, ge, w1, w2, reprw1, reprw2')
    func = input()
    if func == 'eq': print(w1 == w2)
    elif func == 'ne': print(w1 != w2)
    elif func == 'lt': print(w1 < w2)
    elif func == 'gt': print(w1 > w2)
    elif func == 'le': print(w1 <= w2)
    elif func == 'ge': print(w1 >= w2)
    elif func == 'w1': print(w1)
    elif func == 'w2': print(w2)
    elif func == 'reprw1': print(repr(w1))
    elif func == 'reprw2': print(repr(w2))
    elif func != '': print('Такой операции нет')