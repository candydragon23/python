a,b,c,d = map(int, input().split())
l = [[i * g for g in range (a, b+1)] for i in range(c, d+1)]
for row in l:
    print(*row)