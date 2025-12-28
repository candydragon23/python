<<<<<<< HEAD
words = [i for i in input().split()]
dir = {}
maxi = 0
mini = 10000
for k in words:
    if dir.get(k) != None:
        dir[k] += 1
    else:
        dir.update({k : 1})
for k in  dir:
    maxi = max(maxi, dir[k])
    mini = min(mini, dir[k])
print(maxi, mini)
=======
words = [i for i in input().split()]
dir = {}
maxi = 0
mini = 10000
for k in words:
    if dir.get(k) != None:
        dir[k] += 1
    else:
        dir.update({k : 1})
for k in  dir:
    maxi = max(maxi, dir[k])
    mini = min(mini, dir[k])
print(maxi, mini)
>>>>>>> 63c7ffae89fbfaaec9e253afa5cfa1b29a3078a2
