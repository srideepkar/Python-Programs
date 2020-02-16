str1=input("Enter the 1st String: ")
v={"a","e","i","o","u"}
count = 0
for i in str1:
    if(i in v):
        count+=1
print(count)
