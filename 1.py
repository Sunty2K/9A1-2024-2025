import math
c=0;
l=0;
a=list(map(int,input().split()))
s=sum(a)
for i in a:
    if(i%2==0):
        c+=1;
    else:
        l+=1;
if(s%2==0 and c>l):
    print("Ưu thế chẵn");
if(s%2!=0 and c<l):
    print("Ưu thế lẽ");
else:
    print("MÉO PHẢI 1 TRONG 2 CÁI TRÊN ");