import math
n,m=map(int,input().split())
pa,pb=map(int,input().split())
low,high,ans,mid=0,10**8,0,0
while low <= high:
    mid=int((low+high)//2)
    if m+mid*(pa+pb)>=n:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)