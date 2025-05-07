def solve(n, m, k, s):
    s = list(s)
    ans = 0
    i = 0
    while i <= n - m:
        # Kiểm tra đoạn dài m có toàn là '0'
        if all(s[j] == '0' for j in range(i, i + m)):
            # Thao tác tại vị trí i + m - k để đảm bảo phần cuối của đoạn m bị xóa
            pos = min(i + m - 1, n - 1) - k + 1
            pos = max(pos, i)  # Đảm bảo không ra ngoài bên trái
            for j in range(pos, min(pos + k, n)):
                s[j] = '1'
            ans += 1
            i = pos + k  # Bỏ qua đoạn đã xử lý
        else:
            i += 1
    return ans

# Xử lý nhiều test
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    s = input()
    print(solve(n, m, k, s))
