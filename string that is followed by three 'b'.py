import re
n=input("Enter the String: ")
regex=re.compile(r'b{3}?')
if(regex.search(n)== None):
    print("Invalid")
else:
    print("Valid")
