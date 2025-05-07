import sys
sys.stdin=open("GAPNHAU.INP","r")
sys.stdout=open("GAPNHAU.OUT", "w")

from math import lcm

n = int(input())
a, b = map(int, input().split())


print(n//(lcm(a,b)))
