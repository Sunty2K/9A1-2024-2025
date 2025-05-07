n, a, s, ans = int(input()), sorted([int(i) for i in input().split()]
), 0, 0
for i in a:
    if s <= i: s, ans = s + i, ans + 1
print(ans)

