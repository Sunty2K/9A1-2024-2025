b, x = map(str, input().split())
b = int(b)
ans = 0
for i in x:
    ans = ans * b + int(i)
print(ans)
