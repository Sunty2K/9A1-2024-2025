import sys
sys.stdin=open("PASSWORD.INP", "r")
sys.stdout=open("PASSWORD.OUT", "w")

def nt(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

def tach(s_2):
    s = set()
    n = len(s_2)
    for i in range(n):
        for j in range(i+1, min(i+7, n+1)):
            s.add(int(s_2[i:j]))
    return s

t = input()+"#"

nums = []
tmp = ""
for i in t:
    if i.isdigit():
        tmp += i
    elif tmp:
        nums.append(tmp)
        tmp = ""

ans = -1
for i in nums:
    s = tach(i)
    for j in s:
        if nt(j):
            ans = max(j, ans)


print(ans)
