from threading import Thread
def uc(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if n / i != i:ans.append(n/i)
    return len(ans)
def xao(n):
    tmp, a = "", sorted(str(n), reverse = Falsed)
    for i in a: tmp += i
    return tmp
#main!?
n, ans, Falsed = abs(int(input())), [], True

w1 = Thread(target = uc, args=n,)
w2 = Thread(target = xao, args=n,)
w1.start()
w2.start()
w1.join()
w2.join()

print(w1(n))
print(len(str(n)))
print(max(str(n)))
print(w2(n))