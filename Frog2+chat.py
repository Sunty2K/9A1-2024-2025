import sys
import heapq

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    
    dp = [float('inf')] * n
    dp[0] = 0  # Bắt đầu tại hòn đá 0 (tức hòn đá thứ nhất)

    for i in range(1, n):
        for j in range(max(0, i-k), i):
            dp[i] = min(dp[i], dp[j] + abs(h[i] - h[j]))

    print(dp[-1])

if __name__ == "__main__":
    solve()
