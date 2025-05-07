n = int(input())
for i in range(1<<n):
    tmp = ""
    for j in range(n-1, -1, -1):
        tmp += str((i>>j)&1)
    print(tmp)