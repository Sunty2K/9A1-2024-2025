def san():
    x[0], x[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        if x[i] == 1:
            nt.append(i)
            for j in range(i*i, n, i):
                x[j] = 0

def uoc():
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i in nt:
                uc1.append(i)
            else: uc2.append(i)
            if n % (n // i) == 0:
                if ((n // i) in nt):
                    uc1.append(n // i)
                else:
                    uc2.append(n // i)

n = int(input())
x = [1]*(n+1)
nt = []
uc1 = []
uc2 =[]
san()
uoc()

print(len(uc1))
print(len(uc2))
