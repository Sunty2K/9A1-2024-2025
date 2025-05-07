n = int(input())
adj = [[] for i in range(n+1)]
nxt = 0
a = [0] + [int(i) for i in input().split()]
for i in range(1, n+1):
    nxt = i + 1
    while nxt <= n and a[nxt] != a[i]:
        nxt += 1
    if nxt > n:
        adj[i].append(nxt)
    else:
        for t in range(i+1, nxt+1):
            adj[i].append(t)

step = [0]*(n*2)
step[1] = 1
q = [1]
first, lst, ans= 0, 0, 0
while first <= lst:
    if ans > 0:
        break
    i = q[first]
    first += 1
    for j in adj[i]:
        if step[j] == 0:
            step[j] = step[i] + 1
            q.append(j)
            lst += 1
            if j == n:
                ans = step[n] - 1
                break

print(ans)