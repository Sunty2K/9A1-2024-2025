a = int(input())
b = int(input())
u = int(input())
v = int(input())
x = int(input())
y = int(input())
x = x - y
l = 0
n = 0
if a + b <= u + v:
    l = a*x
    n = b*y
else:
    l = u*x
    n = v*y
print(l+n)