def doi(x, y):
    a.remove(x)
    i = a.index(y)
    a.insert(i,x)
n, k = map(int, input().split())
a = [int(x) for x in range(1, n+1)]
for i in range(k):
    x, y = map(int, input().split())
    doi(x,y)
print(*a, sep = " ")