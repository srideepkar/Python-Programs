n=int(input("Enter the Number: "))
p=n
s=0
while(p!=0):
    rem=p%10
    s=int(s+(rem**3))
    p=int(p/10)
if(s==n):
    print("Armstrong")
else:
    print("Not Armstrong")
