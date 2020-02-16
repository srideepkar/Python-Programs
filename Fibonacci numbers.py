def fibbo(n):
    if(n==1):
        print ("0")
    elif(n==2):
        print ("1")
    else:
        count=3
        a=0
        print("0")
        b=1
        print("1")
        while(count!=n+1):
            count+=1
            c=a+b
            print(c)
            a=b
            b=c
a=int(input("Enter Number: "))
x=fibbo(a)



