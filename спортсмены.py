m, n = map(int, input().split())
l = [[int(i) for i in range(m)] for g in range(n)]
res = map(sum, l)
print(res)
print(list((res).index(max(res))))