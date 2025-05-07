import sys
sys.stdin=open("CLB.INP", "r")
sys.stdout=open("CLB.OUT", "w")
n = int(input())
x = [0]*(2*10**3)

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        x[j] += 1

print(max(x))