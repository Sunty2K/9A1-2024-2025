import sys
sys.stdin=open("BANGSO.INP", "r")
sys.stdout=open("BANGSO.OUT", "w")

n , k = map(int, input().split())

if int(k**0.5) == k**0.5:
    print(1)
else:
    print(2)