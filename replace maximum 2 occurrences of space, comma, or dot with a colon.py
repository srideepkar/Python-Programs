import re
p=input("Enter address: ")
print(re.sub('[" "]{2}|[","]{2}|["."]{2}',':',p))
