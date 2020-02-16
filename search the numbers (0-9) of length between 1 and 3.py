import re
n=input("Enter the String: ")
regex=re.compile(r'[0-9]{1,3}')
if(regex.search(n)== None):
    print("Invalid")
else:
    print("Valid")
