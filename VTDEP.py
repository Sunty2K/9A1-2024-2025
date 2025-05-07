import sys
sys.stdin=open("VTDEP.INP", "r")
sys.stdout=open("VTDEP.OUT", "w")

m, n = map(int, input().split())
a = [[0]*(n+1)]+[[0]+[int(i) for i in input().split()]+[0] for _ in range(m)]+[[0]*(n+1)]
ans = 0
for i in range(1, m):
    for j in range(1, n):
        if a[i][j] > a[i+1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i-1][j] and a[i][j] > a[i][j-1]:
            ans += 1
print(ans)