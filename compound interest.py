def si(p,r,t):
        si=p*(1+(r/100)**t)
        return(si)
p=eval(input("Enter the principal: "))
r=eval(input("Enter the rate of interest: "))
t=eval(input("Enter the time: "))
x=si(p,r,t)
i=x-p
print(i)
