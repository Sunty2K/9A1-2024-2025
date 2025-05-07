def check(x, y, c):
    x.sort()
    y.sort()
    for i in range(1, c):
        if x[i] - y[i] != x[i+1] - y[i-1]:
            return False
    return True

def check2(x, y, c):
    tmp = x[1]
    tmp2 = y[1]
    for i in range(1, c+1):
        x[i] -= tmp
        y[i] -= tmp1
    if x != y: return False
    return True

a, b, ans = [0], [0], []

n = int(input())# độ dài mảng xét
for _ in range(n):
    tmp = int(input())
    a.append(tmp)# mảng xét

c = int(input())# độ dài mảng mẫu
for _ in range(c):
    tmp = int(input())
    b.append(tmp)# mảng mẫu

for i in range(1, n-c+1):
    if check(a[i:i+c], b, c) or check2(a[i:i+c, b, c]):
        ans.append(i)
print(len(ans))
for i in ans:
    print(i, end="")
print()