n, ans = int(input()), 0
a = n // 5
if n in [1, 2, 3, 4, 7]: ans = -1
elif n % 5 == 0: ans = n // 5
elif n % 5 == 1: ans = a + 1
elif n % 5 == 2: ans = a + 2
elif n % 5 == 3: ans = a + 1
elif n % 5 == 4: ans =  + 2
else: ans = -1

print(ans)