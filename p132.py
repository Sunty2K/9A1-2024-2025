def check(i):
    global n, mn
    low, high, ans = 0, len(mn), -1
    while(low <= high):
        mid = (low+high)//2
        if a[mid] > i:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

n = int(input())
a = [0]+[int(i) for i in input().split()]
mn = [0]
for i in range(n):
    tmp = check(a[i])
    if i != 0 and tmp != -1:
        mn[tmp] = a[i]
    else:
        mn.append(a[i])
print(len(mn)-1)
