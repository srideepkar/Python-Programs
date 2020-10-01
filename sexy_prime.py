import math
def prime(digit):
    num=digit
    if num>1:
        for i in range(2,math.ceil(math.sqrt(num))+1):
            if (num%i)==0:
                return 0
        return digit
minimum=int(input("lower range: "))
maximum=int(input("Upper range: "))
count=0
for i in range(minimum,maximum):
    x=prime(i)
    #print(x)
    y=prime(x+6)
    #print(y)
    if(x!=0 and y!=0):
        if(y<maximum):
            #print(x)
            #print(y)
            count+=1
if count>0:
    print(count)
else:
    print("No prime pairs")