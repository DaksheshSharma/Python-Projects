#Python Calculator
for i in range (1,501):
    a = float(input("Enter 1st no : "))
    b = float(input("Enter 2nd no : "))
    c = input ("Enter operation : ")
    if c == '+' or c == '-' or c == '*' or c == '/':
        if c == '+':
            print(f"The result of addition of {a} and {b} is {a + b}.") 
        if c == '-' :
            print(f"The result of subtraction of {a} and {b} is {a - b}.")
        if c == '*':
            print(f"The result of multiplication of {a} and {b} is {a * b}.")
        if c == '/' :
            if b != 0 :
                print(f"The result of division of {a} and {b} is {a / b}.")
            if b == 0:
                print(f"The result of division of {a} and {b} is infinity. ") 
    else:
        print ("Enter a valid operation.")