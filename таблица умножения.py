<<<<<<< HEAD
a,b,c,d = map(int, input().split())
l = [[i * g for g in range (a, b+1)] for i in range(c, d+1)]
for row in l:
=======
a,b,c,d = map(int, input().split())
l = [[i * g for g in range (a, b+1)] for i in range(c, d+1)]
for row in l:
>>>>>>> 63c7ffae89fbfaaec9e253afa5cfa1b29a3078a2
    print(*row)