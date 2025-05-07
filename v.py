ans=0
n, k=map(int,input().split())
d=dict()
for i in range(0,n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        d[j]=d.get(j,0)+1
for i in d:
    if(d.get(i)==k):
        ans+=1
print (ans)