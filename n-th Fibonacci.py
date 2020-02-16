def fibbo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        count=3
        a=0
        b=1
        while(count!=n+1):
            count+=1
            c=a+b
            a=b
            b=c
        return c
a=int(input("Enter Number: "))
x=fibbo(a)
print(x)



