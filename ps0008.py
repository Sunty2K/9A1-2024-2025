n, k = map(int, input().split())
a = [int(i) for i in input().split()]
s = a[0]
a = sorted(a[1::], reverse = True)
i = n - k - 1
j = n - 1

print(s + sum(a[:k])-sum(a[k:]))