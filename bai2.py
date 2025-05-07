a, b, c, k = map(int,input().split())
print(min(a, b, c))
print(max(a*b, b*c, a*c) % k)