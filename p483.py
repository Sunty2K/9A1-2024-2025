snt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

ans, n = 0, int(input())
for i in [int(_) for _ in input().split()]:
    if sum(map(int, str(i))) in snt: ans += 1
print(ans)
