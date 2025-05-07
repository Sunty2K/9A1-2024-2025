

def snt(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True


n = int(input())
nt = [2, 3, 5, 7, 11, 17]
hh = []
a = [int(i) for i in input().split()]
for p in nt:
    if snt(2**p - 1):
        hh.append(2**(p-1)*(2**p-1))
ans = 0
for x in a:
    if x in hh: ans += 1
print(ans)