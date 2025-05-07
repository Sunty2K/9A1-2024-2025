# import sys
# sys.stdin=open("TIMKT.INP", "r")
# sys.stdout=open("TIMKT.OUT", "w")
a = [0]*(26)

for i in input():
    a[ord(i) - ord("A")] += 1
mx = max(a)
for i in range(27):
    if a[i] == mx:
        print(chr(i+ord("A")))
        break