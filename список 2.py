list1 = [int(i) for i in input().split()]
list2 = [int(k) for k in input().split()]
print(*[pair[1] - pair[0] for pair in zip(list1, list2)])