# This is the simple code to find the greater numbers from entered two numbers
print("Enter two numbers:")
num1=int(input("1."))
num2=int(input("2."))
if num1 != num2 :
    if num1 > num2 :
        print(str(num1) + " is max!")
    else: print(str(num2) + " is max!")
else: print("Both are same!")