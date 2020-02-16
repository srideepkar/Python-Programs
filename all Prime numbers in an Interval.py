def prime(n):
    count=0
    for i in range(2,n,1):
        if(n%i==0):
            count+=1
    if(count==0):
        return 1
    else:
        return 0    
a=int(input("Enter upper Range: "))
b=int(input("Enter lower Range: "))
for i in range(a,b+1,1):
    x=prime(i)
    if(x==1):
        print(i)



