str1=input("Enter the String: ")
l=[]
l=str1.split()
for i in l:
    if(len(i)%2==0):
        print(i)
