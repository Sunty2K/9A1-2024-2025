import math

n=str(input())
for i in range (0,len(n)+1):
    if((n[i]=="x") or (n[i]=="X")):
        n[i]="*"
    if(n[i]==":"):
        n[i]="/"
print(eval(n))