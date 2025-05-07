n, cnt = int(input()), [0]*26
for _ in range(n):
    s1, s2 = input().split()
    f1 = [0]*26
    for c in s1: f1[ord(c) - ord("a")] += 1
    f2 = [0]*26
    for c in s2: f2[ord(c) - ord("a")] += 1
    for j in range(26): cnt[j] += max(f1[j], f2[j])
for x in cnt: print(x)