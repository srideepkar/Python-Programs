import re
str1=input("Enter the 1st String: ")
regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(regex.search(str1)== None):
    print("NO Special Character")
else:
    print("Special Characters found")
