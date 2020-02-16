def factorial1(n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return(fact)
n=eval(input("Enter the number: "))
x=factorial1(n)
print(x)
