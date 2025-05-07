import sys
sys.stdin=open("MUAHE.INP", "r")
sys.stdout=open("MUAHE.OUT", "w")

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
ans = 0
i = 0
j = 0

while(i < n and j < n):
    if sum(a[i:j+1]) <= k and j - i + 1 > ans:
        ans = j - i + 1
    elif sum(a[i:j+1]) > k:
        i += 1
    else: j += 1

print(ans)
