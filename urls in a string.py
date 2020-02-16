import re
p=input("Enter string: ")
regex=re.compile(r'[a-zA-z].[a-zA-Z0-9].com')
if(regex.search(p)!=None):
    print("URL found")
else:
    print("Not found")
