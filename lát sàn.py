from math import sqrt
g, y = map(int, input().split())

low, high = 1, int(sqrt(g + y))
while low <= high:
    m = (low + high)// 2 
    n = (g + 4)//2 - m     
    if (m * n == g + y) and ((g + y) % n == 0):
        print(m, n, end="\n")
        break
    if m * n < g + y:
        low = m + 1
    else:
        high = m - 1