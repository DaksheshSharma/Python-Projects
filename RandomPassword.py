#Made by Dakshesh Sharma
#https://github.com/DaksheshSharma/Python-Projects
import random
for i in range(1,501):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '123456789'
    symbol = '_'
    length = int(input("Length of password : "))
    if length > 20 or length == 20:
        print("Enter a no less than 20")
    if length < 20 :
        all = lower + upper + number + symbol
        password = "".join(random.sample(all,length))
        print(f"The password you generated is {password}")