str1=input("Enter the 1st String: ")
l=[]
c=0
count=0
for i in str1:
    for j in str1:
        if(i==j):
            count+=1
    if(count==1):
        l.append(i)
    else:
        for j in l:
            if(j==i):
                c+=1
        if(c==0):
            l.append(i)
        c=0
    count=0
print("".join(l))
        
