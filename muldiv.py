def isqrt(n): return int(n**0.5)

def check(n):
    s = 1
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            s *= i
            if n % (n//i) == 0:
                s *= (n//i)
    return s

m = int(input())
n = 1
for j in ([int(i) for i in input().split()]
):
    n *= j
print(check(n))