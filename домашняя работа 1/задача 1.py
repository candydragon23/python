l = [int(i) for i in input().split()]
print(*[l[i-1] + l[(i+1) % len(l)] for i in range(len(l))]) if len(l) > 1 else print(*l)