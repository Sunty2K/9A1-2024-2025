n, k = map(int, input().split())
h = [0] + list(map(int, input().split()))
d = [float("inf")] * (n + 1)
d[1] = 0

for i in range(2, n + 1):
    for j in range(max(1, i - k), i):
        d[i] = min(d[i], d[j] + abs(h[i] - h[j]))

print(d[n])