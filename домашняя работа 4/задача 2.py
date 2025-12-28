n = int(input())
dict1 = {}
for _ in range(n):
    arr = input().split()
    dict1.update({arr[0] : arr[1]})
    dict1.update({arr[1] : arr[0]})
print(dict1[input()])