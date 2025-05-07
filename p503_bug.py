
def nhiphan(n):
    if n < 0:
        return []
    np = []
    for i in range(1 << n):
        tmp = ""
        for j in range(n - 1, -1, -1):
            tmp += str((i >> j) & 1)
        np.append(tmp)
    return np

def check1(s, m):
    tmp = s[0]
    cnt = 1
    for i in s[1:]:
        if i != tmp:
            if cnt >= m: return False
            cnt = 1
            tmp = i
        else:
            cnt += 1
            if cnt >= m: return False
    return True

def check2(s, m):
    if not s:
        return True
    if m <= 0:
        return True
    if m == 1 and len(s) >= 1:
        return False

    tmp = s[0]
    cnt = 1
    for i in s[1:]:
        if i == tmp:
            cnt += 1
        else:
            if cnt >= m:
                 return False
            tmp = i
            cnt = 1
        if cnt >= m:
            return False
    return True

def check(s, m):
    return check1(s, m) and check2(s, m)

def dao(s, k, np):
    s = list(s)
    for i in range(len(np)):
        if np[i] == "1":
            for j in range(i, i + k):
                s[j] = "1" if s[j] == "0" else "0"
    return ''.join(s)

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    s = input()
    ans = 10**9 + 7

    if check(s, m):
        print(0)
    else:
        np = nhiphan(n-k)

        found = False

        for i in np:
            a = dao(s, k, i)
            if check(a, m):
                found = True
                tmp = i.count("1")
                ans = min(ans, tmp)

        if found:
            print(ans)
        else:
            print(-1)