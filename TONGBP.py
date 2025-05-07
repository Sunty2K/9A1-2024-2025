import sys
sys.stdin=open("TONGBP.INP", "r")
sys.stdout=open("TONGBP.OUT", "w")
s = input()
ans = 0
for i in s:
    ans += int(i)**2
print(ans)