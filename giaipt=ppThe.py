v1,t1,s1=map(int,input().split())
v2,t2,s2=map(int,input().split())
x=y=0
y=(s2*v1-s1*v2)//(-t1*v2+t2*v1)
x=(s1-y*t1)//v1
print (x*2)
print(y*2)
