import sys
sys.stdout=open("find_fibo.py","w")

mod = 10**9+7
n = int(input())
a, b, c = 1, 1, 1
print("fibo = [ 0 , 1 , 1 ", end = "")
for i in range(3, n+1):
    tmp = (a + b)%mod
    a = b
    c = tmp
    b = c

    print(f", {c}", end = " ")
    if i % 20 == 0:
        print("\n         ")
print("\n       ]")

print("""
n = int(input())
print(fibo[n]%(10**9+7))
""")