import sys
sys.stdin=open("VITRI.INP","r")
sys.stdout=open("VITRI.OUT","w")

def check(ss):
    tmp_1, tmp_2 = ss[0], ss[1:]
    if " " not in ss:
        if tmp_1 == tmp_1.upper() and tmp_2 == tmp_2.lower():
            return False
    return True

n = int(input())
for i in range(1, n+1):
    ans = 0
    s = input()
    if check(s):
        print(i, end = " ")
        ans = 1

if ans == 0: print(0)
else: print()
