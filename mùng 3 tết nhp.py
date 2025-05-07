n = int(input())
x = [int(_) for _ in input().split()]

p_1 = min(n-1, sum(x)//n)
p_2 = p_1 + 1

tot_1 = sum([(xi - p_1)**2 for xi in x])
tot_2 = sum([(xi - p_2)**2 for xi in x])

print(min(tot_1, tot_2))