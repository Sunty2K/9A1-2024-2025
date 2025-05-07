from math import gcd
b = (999996 - 100002)//6+1
a = 999999-100000+1
lờ_cờ_mờ = (a*b) // gcd(a, b)
print(f"{lờ_cờ_mờ//a}\n-\n{lờ_cờ_mờ//b}")