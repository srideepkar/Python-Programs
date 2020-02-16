def prime(n):
    count=0
    for i in range(2,n,1):
        if(n%i==0):
            count+=1
    if(count==0):
        return 1
    else:
        return 0    
a=int(input("Enter Number: "))
x=prime(a)
if(x==1):
    print("Prime")
else:
    print("Non prime")



