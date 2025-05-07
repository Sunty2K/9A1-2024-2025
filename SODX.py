# import sys
# sys.stdin=open("SODX.INP", "r")
# sys.stdout=open("SODX.OUT", "w")
n, ans = int(input()), 0
for i in [_ for _ in input().split()]:
    if i == i[::-1]: ans += 1
print(ans)
