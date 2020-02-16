import re
p=input("Enter address: ")
print(re.sub('road$','Rd',p))
