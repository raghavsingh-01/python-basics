#This is the simple block of code to calculate the sum of digits
n = int(input("Enter a number :"))
l = len(str(n))

sum = 0
while l > 0 :
    d = n%10
    n = n//10
    sum = sum+d
    l = l - 1
print("The Sum of digits is :" + str(sum))