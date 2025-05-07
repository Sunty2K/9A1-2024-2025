n, m, k = map(int, input().split())

x = str(n * m * k)[::-1]

if len(x) >= 2 and x[0] == "0":
    print("YES")
else: print("NO")