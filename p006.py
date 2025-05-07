n, m = map(int, input().split())

a = ["#"*(m+1)] + ["#" + input() for i in range(n)]
ans = []
for i in range(1, n+1):
    tmp = ""
    found = False
    for j in range(1, m+1):
        if a[i][j] != "#":
            tmp += a[i][j]
            found = True
        else:
            if len(tmp) >= 2:
                ans.append(tmp)
                found = False
            tmp = ""
    if found:
        if len(tmp) >= 2:
            ans.append(tmp)

for i in range(1, m+1):
    tmp = ""
    found = False
    for j in range(1, n+1):
        if a[j][i] != "#":
            tmp += a[j][i]
            found = True
        else:
            if len(tmp) >= 2:
                ans.append(tmp)
                found = False
            tmp = ""
    if found:
        if len(tmp) >= 2:
            ans.append(tmp)
print(min(ans))