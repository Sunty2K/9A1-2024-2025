import sys
sys.stdin.readline

n, k = map(int, input().split())

x = [0]*(n+2)

for _ in range(k):
    a, b = map(int, input().split())
    x[a] += 1
    x[b+1] -= 1

tmp = 0
for i in range(1, n+1):
    tmp += x[i]
    x[i] = tmp
x = sorted(x[:n+1])
print(x[n//2+1])