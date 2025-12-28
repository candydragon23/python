x,y = map(int, input().split())
ad = [input() for _ in range (x)]
tabl = [input().split() for _ in range(x)]
for y1 in range(y):
    for x1 in range(x):
        cur = ad[y1][x1]
        if cur != "." and cur == "R" and tabl[y1][x1] != '4' and tabl[y1][x1] != '5' and tabl[y1][x1] != '6' and tabl[y1][x1] != '7':
            print("NO")
            exit(0)
        elif cur == "B" and tabl[y1][x1] != '1' and tabl[y1][x1] != '3' and tabl[y1][x1] != '5' and tabl[y1][x1] != '7':
            print("NO")
            exit(0)
        elif cur == "G" and tabl[y1][x1] != '2' and tabl[y1][x1] != '3' and tabl[y1][x1] != '6' and tabl[y1][x1] != '7':
            print("NO")
            exit(0)
print("YES")