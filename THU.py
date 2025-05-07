import sys
sys.stdin=open("THU.INP", "r")
sys.stdout=open("THU.OUT", "w")

def check1(s):
    return s[::-1]
def check2(s):
    return s
n = int(input())
s = input()[::-1]
tmp = ""
ans = ""
for i in s:
    if i == "1":
        ans += " " + check2(tmp)
        tmp = ""
    elif i == "2":
        ans += " " + check1(tmp)
        tmp = ""
    else: tmp += i

print(ans[::-1])