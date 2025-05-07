import math

a,b,c=map(int,input().split())
de=b**2-4*a*c
if(de <0):
    print("N/a")
elif(de ==0):
    print("X = ", -1*b/(2*a))
elif(de > 0):
    print("X1 = ", (-1*b-math.sqrt(de))/(2*a))
    print("X2 = ", (-1*b+math.sqrt(de))/(2*a))