import sys
sys.stdin=open("DATHUC.INP", "r")
sys.stdout=open("DATHUC.OUT", "w")
n, x = map(int, input().split())
a = [int(i) for i in input().split()]
s = 0
for i in range(n, -1, -1):
    s += a[i]*x**(n-i)
print(s)