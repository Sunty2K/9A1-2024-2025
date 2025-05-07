s = input()
ans, tong, tmp = 0, 0, 0

for i in s:
    if "0" <= i <= "9":
        tmp *= 10
        tmp += int(i)
        ans += 1

    else:
        tong += tmp
        tmp = 0

if "0" <= s[len(s)-1] <= "9": tong += tmp

print(ans)
print(tong)