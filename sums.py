n , s = map(int, input().split())
ans = 0
a = [int(i) for i in input().split()]
used = []
for i in range(n):
    if (s-a[i]) in a:
        tmp = a.index(s - a[i])
        if tmp != i and [i, tmp] not in used:
            ans += 1
            used.append([i, tmp])
            used.append([tmp, i])
            print(i, tmp)
print(ans)