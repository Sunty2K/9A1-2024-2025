n = int(input())
a = [0] + [int(i) for i in input().split()]
pos = [0]*(3*10**5 + 1)
nxt = [0]*(3*10**5 + 1)

for i in range(n, 0, -1):
    nxt[i] = pos[a[i]]
    pos[a[i]] = i

mx = 1
nx = nxt[1]
ans = 0
for i in range(2, n+1):
    if i > nx:
        ans = 0
        break
    if i > mx:
        ans += 1
        mx = nx
    nx = max(nx, nxt[i])
    
print(ans)