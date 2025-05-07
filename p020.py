n = int(input())
a = [int(i) for i in input().split()]
print(max(sum(a[::2]), sum(a[1::2])))