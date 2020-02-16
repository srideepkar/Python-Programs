import re
n=input("Enter the String: ")
regex=re.compile(r'[a-zA-Z0-9]')
if(regex.search(n)!= None):
    print("valid")
else:
    print("Invalid")
