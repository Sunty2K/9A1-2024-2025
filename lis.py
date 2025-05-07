n = int(input())
a = [0]+[int(i) for i in input().split()]
cur = []
lis = []

def sinh(i):
    global cur, lis
    if i > n:
        if len(cur) > len(lis):
            lis = cur.copy()
        return

    if len(cur) == 0 or a[i] > cur[-1]:
        cur.append(a[i])
        sinh(i+1)
        cur.pop()

    sinh(i+1)

sinh(1)
print(len(lis))