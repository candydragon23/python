n = int(input())
dict1 = {}
for _ in range (n):
    arr = input().split()
    for _ in range(1, len(arr)): dict1.update({arr[_] : arr[0]})
m = int(input())
arrout = input().split()
for _ in range (m):
    print(dict1[arrout[_]])