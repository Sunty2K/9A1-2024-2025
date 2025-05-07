n , W = map(int, input().split())
w = [int(i) for i in input().split()]
v = [int(i) for i in input().split()]
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        if j >= w[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][W])
