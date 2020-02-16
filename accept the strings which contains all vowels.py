str1=input("Enter the String: ")
l=[]
l[:0]=str1
count=0
for i in l:
    if(i!="a" and i!="e" and i!="i" and i!="o" and i!="u"):
        count+=1
if(count==0):
    print(str1)
    
