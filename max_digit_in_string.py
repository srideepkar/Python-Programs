total_test=int(input("Enter the total number of test case: "))
for i in range(total_test):
    inp_string=input("Enter the input string: ")
    digit=[]
    for i in inp_string.split():
        if i.isdigit()==True:
            digit.append(i)
    max_digit=digit[0]        
    for i in digit:
        if i>max_digit:
            max_digit=i            
    print(max_digit)