x, b = map(int, input().split())
ans = []
while(x > 0):
    ans.append(x % b)
    x = b
for i in ans[::-1]:
    print(i, end = "")
print()