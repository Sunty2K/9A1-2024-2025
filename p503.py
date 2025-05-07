# 1 2 3 4 5 6 7 8 9 | 11 22 33 44 55 66 77 88 99 | 111 222 333 444 

def check(s):
    return len(set(s)) == 1

def check2(s):
    tmp = s[0] * len(s)
    if tmp > s:
        return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    s = str(n)
    ans = 0
    if len(s) == 1:
        print(n)
    else:
        if check(s):
            ans = 9 * (len(s)-1) + int(s[0])
        else:
            if check2(s):
                ans = 9 * (len(s)-1) + int(s[0])
            else:
                ans =  9 * (len(s)-1) + int(s[0])-1

        print(ans)
