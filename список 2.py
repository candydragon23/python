<<<<<<< HEAD
list1 = [int(i) for i in input().split()]
list2 = [int(k) for k in input().split()]
=======
list1 = [int(i) for i in input().split()]
list2 = [int(k) for k in input().split()]
>>>>>>> 63c7ffae89fbfaaec9e253afa5cfa1b29a3078a2
print(*[pair[1] - pair[0] for pair in zip(list1, list2)])