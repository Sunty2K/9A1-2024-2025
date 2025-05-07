import sys
sys.stdin=open("QUA.INP", "r")
sys.stdout=open("QUA.OUT", "w")

n, k = map(int, input().split())
a = sorted([int(i) for i in input().split()], reverse = True)

print(sum(a[:k]))