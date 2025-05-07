def nhiphan(n):
    np = []
    for i in range(1<<n):
        tmp = []
        for j in range(n-1, -1, -1):
            tmp.append((i>>j)&1)
        np.append(tmp)
    return np

def check(nums):
    digit = [0]*15
    cnt = 0
    for num in nums:
        for i in range(15):
            digit[i] += num % 10
            if digit[i] >= 10:
                return 0
            num //= 10
            if num == 0:
                cnt += 1
                break
    return cnt

a = []
n = int(input())
np = nhiphan(n)
for i in range(n):
    a.append(int(input()))
ans = -1
for i in np:
    tmp = []
    if sum(i) <= ans: continue
    for j in range(n):
        if i[j] == 1:
            tmp.append(a[j])
    ans = max(check(tmp), ans)
print(ans)
