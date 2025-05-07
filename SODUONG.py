import sys
sys.stdin=open("SODUONG.INP", "r")
sys.stdout=open("SODUONG.OUT", "w")

mn = 10**9-7
n = int(input())
for i in range(n):
    a = int(input())
    if a > 0:
        mn = min(mn, a)
print(mn)