w,h = [int(_) for _ in input().split()]
n = int(input())
li = [[0 for _ in range(h)] for _ in range (w)]
for _ in range (n):
    col_1, row_1, col_2, row_2 = [int(_) for _ in input().split()]
    for y in range(row_1, row_2):
        for x in range(col_1, col_2):
            li[y][x] = 1
print(sum(row.count(0) for row in li))