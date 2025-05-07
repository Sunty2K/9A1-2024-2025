import sys
sys.stdin=open("TRAVANG.INP", "r")
sys.stdout=open("TRAVANG.OUT", "w")
n, m = map(int, input().split())
a = [int(i) for i in input().split()]
i = 0
j = 0
ans = 0
while(i < n):
    if sum(a[i:j+1]) <= m and j < n:
        ans += 1
        j += 1
    else:
        i += 1
        j = i
print(ans)