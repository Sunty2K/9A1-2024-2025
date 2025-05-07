import sys
sys.stdin=open("LAPDAT.INP", "r")
sys.stdout=open("LAPDAT.OUT", "w")

t = int(input())
a = 400+50*t
b = 90*t
if a > b:
    print("B")
    print(b)
else:
    print("A")
    print(a)