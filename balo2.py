def unbounded_knapsack(n, W, w, v):
    dp = [0] * (W + 1)
    
    for j in range(W + 1):  # trọng lượng hiện tại
        for i in range(n):  # xét từng món
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])

    return dp[W]

# Ví dụ
n = 4
W = 8
w = [3, 4, 5, 2]  # trọng lượng
v = [2, 3, 4, 2]  # giá trị

print("Giá trị tối đa:", unbounded_knapsack(n, W, w, v))  # Kết quả: 8
