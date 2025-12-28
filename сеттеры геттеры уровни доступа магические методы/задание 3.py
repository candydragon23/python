class IPAddress:
    def __init__(self, ipaddress):
        self.ip = ipaddress

    def __str__(self):
        return self.ip

    def __repr__(self):
        return f'IPAddress(\'{self.ip}\')'

print('Введите первый IP адрес')
ip = input()
print('Введите второй IP адрес')
IP1 = IPAddress(ip)
ip = input()
IP2 = IPAddress(ip)
print('Строковое представление первого IP адреса')
print(IP1)
print(repr(IP1))
print('Строковое представление второго IP адреса')
print(IP2)
print(repr(IP2))
