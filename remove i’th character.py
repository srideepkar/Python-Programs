n=input("Enter string: ")
l1=[]
l2=[]
count=0
l1[:0]=n
p=int(input("Enter position: "))
for i in l1:
    count+=1
    if(count!=p):
        l2.append(i)
m="".join(l2)
print(m)
