ticket = input()


def numroot (st):
    numsq = sum(int(st[k]) for k in range(len(st)))
    if len(str(numsq)) > 1:
        return numroot(str(numsq))
    else:
        return numsq


for i in range(len(ticket)):
    if numroot(ticket[:i]) == numroot(ticket[i:]):
        print("YES")
        exit(0)
print("NO")