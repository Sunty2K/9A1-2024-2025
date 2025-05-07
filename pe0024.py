s = input()
l = len(s)
s += "#"
i = 0
ans = ""
while(i <= l-1):
    if s[i] != s[i+1]:
        ans += s[i]
        i += 1
    else:
        i += 2
print(ans if  len(ans) != 0 else "Empty String")