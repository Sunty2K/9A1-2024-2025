from math import sqrt
import sys
sys.stdout=open("sntm.py","w")
def nt(n):
    if n < 2: return 0
    if n == 2 or n == 3: return 1
    if n % 2 == 0 or n % 3 == 0: return 0
    for i in range(5, int(sqrt(n)) + 1, 2):
        if n % i == 0: return 0
    return 1

print("snt = [", end = "")
snt = []
cnt = 1
for i in range(2, 82):
    if nt(i) == 1:
        if cnt % 100 == 0:
            print(f"\n        {i}, ", end = "")
            cnt = 1
        print(F"{i}", end = ", ")
        cnt += 1
print("      ]")

print("""
ans = 0
n = int(input())
for i in [int(_) for _ in input().split()]:
    if sum(map(int, str(i))) in snt: ans += 1
print(ans)
""")