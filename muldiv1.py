from collections import Counter
from math import isqrt
import sys
sys.stdin.readline

MOD = 10**9 + 7

def prime_factors(n):
    pf = Counter()
    for p in range(2, isqrt(n)+1):
        while n % p == 0:
            pf[p] += 1
            n //= p
    if n > 1:
        pf[n] += 1
    return pf

m = int(input())
a = list(map(int, input().split()))

# Tính phân tích thừa số nguyên tố của s = tích tất cả phần tử
total_factors = Counter()
product = 1
for x in a:
    product = (product * x) % MOD
    total_factors += prime_factors(x)

# Tính số ước của s
num_divisors = 1
for exp in total_factors.values():
    num_divisors = (num_divisors * (exp + 1)) % (MOD - 1)  # Euler's theorem

# Tính tích tất cả ước: s^(num_divisors // 2)
# Vì num_divisors luôn chẵn (nếu không, phải xử lý cẩn thận)
exponent = num_divisors // 2
result = pow(product, exponent%(MOD-1), MOD)

print(result)
