import sys
sys.stdin=open("DONHANG.INP", "r")
sys.stdout=open("DONHANG.OUT", "w")

def check(mid):
    global a
    s = 0
    for i in a:
        s += mid // i
    return s

n, k = map(int, input().split())


a = [int(i) for i in input().split()]

low, high, ans = 0, 10**9+7, 0
while(low<=high):
    mid = (low+high)//2
    if check(mid) >= k:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)