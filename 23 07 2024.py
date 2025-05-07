'''
s=str(input())
t=len(s)
b=[]
for i in range(1,t):
    s=s[-1]+s[:t-1]
    b.append(s)
b.sort()
for i in b:
    print(i)
'''
# from math import *
# n=str(input())
# 
# dem=0
# i=1
# while(n[i-1]<=n[i]):
#     dem=dem+1
#     i=i+1
# while(n[i-1]>=n[i]):
#     dem=dem+1
#     i=i+1
# if(dem==len(n)):
#     print("YES")
# else:
#     print("NO")
'''
s=str(input())
s1=""
for i in s:
    s1=i+s1
if(s==s1):
    print("TRUE")
else:
    print("NO")
'''
from math import *
s=str(input())
l=len(s)
st=0
ss=0
for i in range(l):
    if(s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='A'):
        ss=ss+1
    if(s[i]>='0' and s[i]<='9'):
        st=st+1
print(ss)
print(st)

