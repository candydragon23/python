<<<<<<< HEAD
m, n = map(int, input().split())
l = [[int(i) for i in range(m)] for g in range(n)]
res = map(sum, l)
print(res)
=======
m, n = map(int, input().split())
l = [[int(i) for i in range(m)] for g in range(n)]
res = map(sum, l)
print(res)
>>>>>>> 63c7ffae89fbfaaec9e253afa5cfa1b29a3078a2
print(list((res).index(max(res))))