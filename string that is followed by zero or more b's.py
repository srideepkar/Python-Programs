import re
n=input("Enter the String: ")
regex=re.compile(r'[0b*?]')
if(regex.search(n)==None):
    print("Invalid")
else:
    print("Valid")
