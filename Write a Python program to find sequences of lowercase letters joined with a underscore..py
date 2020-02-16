import re
n=input("Enter the String: ")
regex=re.compile(r'[a-z]+_[a-z]+$')
if(regex.search(n)== None):
    print("Invalid")
else:
    print("Valid")
