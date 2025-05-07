n = int(input())
a = [0] + [int(i) for i in input().split()]


tot_1, tot_2 = 0, 0
for i in range(1, n+1):
    tot_1 += a[i]
    tot_2 += a[i]**2

min_cost = 10**15+1
for k in range(1, n+1):
    tot_cost = tot_2 - 2*k*tot_1 + n*k**2
    min_cost = min(min_cost, tot_cost)

print(min_cost)