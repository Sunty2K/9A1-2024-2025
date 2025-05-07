mod = 10**9 + 7
b = 0
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    t = ((b%mod**(c%(mod)//2)%(mod-1))%mod)
    if c % 2 == 0:
        b = (t%mod*t%mod)%mod
    else:
        b = (t%mod*t%mod*b%mod)%mod
    r = ((a%mod**(b%(mod-1)//2)%(mod - 1))%mod)
    if b % 2 == 0:
        print((r%mod*r%mod)%mod)
    else:
        print((r%mod*r%mod*a%mod)%mod)
