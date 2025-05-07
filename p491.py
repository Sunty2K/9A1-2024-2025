from math import sqrt
def uoc(n):
    tong = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            tong += i
            j = n//i
            if j > i and j < n:
                tong += j
    return tong


l, r = map(int, input().split())
BestFriend = []
for i in range(l, r):
    for j in range(i+1, r + 1):
        if uoc(i) == j and uoc(j) == i: BestFriend.append([i, j])

print(len(BestFriend))
for i in BestFriend:
    print(*i, sep = " ")
