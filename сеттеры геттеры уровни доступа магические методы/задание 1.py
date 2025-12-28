class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        print(f'Текущий баланс равен: {self.__balance}')

    def deposit(self, amount):
        if amount != -1:
            self.__balance += amount

    def withdraw(self, amount):
        if amount != -1:
            if self.__balance - amount < 0:
                print('На счете недостаточно средств')
            else:
                self.__balance -= amount

    def transfer(self, amount, account):
        if amount != -1:
            if self.__balance - amount < 0:
                print('На счете недостаточно средств')
                return account
            else:
                account += amount
                self.__balance -= amount
                print(f'Внесено {amount} рублей на счет account')
                print(f'Средства счета account: {account}')
                return account

def trynumber():
    try: number = int(input())
    except ValueError:
        print('Необходимо ввести целое число')
        return -1
    if number < 0:
        print('Число должно быть положительным')
        return -1
    return number

func = ' '
account = 0
print('Введите начальный баланс (целое число, по умолчанию 0)')
balancestr = input()
if balancestr == '': balance = 0
else:
    try: balance = int(balancestr)
    except ValueError:
        print('Необходимо ввести целое число')
        exit(-1)
acc = BankAccount(balance)

while func != '':
    print('Выберите действие (ничего не вводите и нажмите enter для прекращения работы)')
    print('Возможные операции: balance, deposit, withdraw, transfer')
    func = input()
    if func == 'balance': acc.get_balance()
    elif func == 'deposit' :
        print('Введите положительную целую сумму для вноса')
        acc.deposit(trynumber())
    elif func == 'withdraw':
        print('Введите положительную целую сумму для снятия')
        acc.withdraw(trynumber())
    elif func == 'transfer':
        print('Введите положительную целую сумму перевода')
        account = acc.transfer(trynumber(), account)
    elif func != '':
        print('Такой операции не существует')