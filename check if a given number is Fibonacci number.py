def fibo(n):
    if(n==0):
        print ("True")
    else:
        count=0
        v=0
        a=0
        b=1
        while(count!=n*2):
            count+=1
            c=a+b
            if(n==c):
                print("True")
                v=1
            a=b
            b=c
        if(v==0):
            print("False")
a=int(input("Enter Number: "))
x=fibo(a)



