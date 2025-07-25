
num = int(input("Enter a number to find multiplication table :"))

print("The multiplication table of " + str(num))
n=1
while n<=10 :
        mul = num * n
        print(str(n) + ". " +str(mul))
        n = n + 1