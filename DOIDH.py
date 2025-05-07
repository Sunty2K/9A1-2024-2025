# import sys
# sys.stdin=open("DOIDH.INP", "r")
# sys.stdout=open("DOIDH.OUT", "w")
n, x = map(int, input().split())
a = sorted([int(i) for i in input().split()])
mx = 0
ans_i, ans_j = 0, 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[j] - a[i] > x: break
        elif j - i > mx:
            ans_i, ans_j = i, j
            mx = j - i

print(ans_j - ans_i + 1)
        
