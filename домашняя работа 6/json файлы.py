import json
file2 = open('output.json', 'w')
print('Введите количество пользователей: ')
n = int(input())
users = {}
current = 1
for _ in range (n):
    print("Введите данные (enter чтобы прекратить ввод)")
    user = {}
    curuser = "user" + str(current)
    while True:
        try:
            key, value = input().split(": ")
            user.update({key : value})
        except ValueError:
            users.update({curuser : user})
            break
    current += 1
json.dump(users, file2)
file2.close()
file2 = open('output.json', 'r')
data = str(json.load(file2))
data = data.replace("}, ", "},\n")
print(data)
file2.close()
