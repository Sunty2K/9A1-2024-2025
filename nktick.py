# import sys
# sys.stdin=open("dpgame2.inp", "r")
# sys.stdout=open("dpgame2.out", "w")

n, k = map(int, input().split())

h = [0]+[int(i) for i in input().split()]
if n > k:
    d = [float("inf")]*(n+1)

    d[0] = float("inf")
    d[1] = 0

    for i in range(2, n+1):
        for j in range(1, k+1):
            d[i] = min(abs(h[i-j] - h[i]) + d[i-j], d[i])

    print(d[n])
else:
    print(h[-1] - h[1])