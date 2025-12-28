class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.fname = firstName
        self.lname = lastName
        self.group = group
        self.mark = averageMark

    @property
    def getScolarship(self):
        if self.mark == 5:
            return 10000
        elif self.mark > 3:
            return 5000
        else:
            return 0

class Undergraduate(Bachelor):

    @property
    def getScolarship(self):
        if self.mark == 5:
            return 15000
        elif self.mark > 3:
            return 7500
        else:
            return 0

students = []
i = 1
while True:
    print('Введите информацию о студентах (введите пустую строку для завершения ввода)')
    print('Формат ввода: имя фамилия группа средний балл')
    student = 'student' + str(i)
    i += 1
    l = [_ for _ in input().split()]
    if not l:
        break
    if len(l) != 4:
        print('Неправильный ввод')
    else:
        try:
            l[3] = float(l[3])
            if l[3] < 0 or l[3] > 5:
                print('Неправильный ввод средней оценки')
            else:
                print('Введите квалификацию (bac, und)')
                qual = input()
                if qual == 'bac':
                    student = Bachelor(*l)
                    students.append(student)
                elif qual == 'und':
                    student = Undergraduate(*l)
                    students.append(student)
                else:
                    print('Такой квалификации нет')
        except ValueError:
            print('Неправильный ввод средней оценки')
i = 1
for student in students:
    print(f'Стипендия студента {i}: {student.getScolarship}')
    i += 1