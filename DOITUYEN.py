import sys
sys.stdin=open("DOITUYEN.INP", "r")
sys.stdout=open("DOITUYEN.OUT", "w")

n = int(input())

a = [int(i) for i in input().split()]


mx = max(a)
ans = 0
for i in a:
    if i >= mx*0.75: ans += 1

print(ans)