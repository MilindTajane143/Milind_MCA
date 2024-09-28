# OWN CODE

num1 = int(input("Enter 1st parameter"))
num2 = int(input("Enter 2nd parameter"))
num3 = int(input("Enter 3rd parameter"))

if (num1 > num2):
    print ("Num1 is greater than num 2 and num 3 ")
elif (num2 > num3):
    print ("Num2 is greater than num 1 and num 3")
elif (num3 > num1):
    print ("Num3 is greater than num 1 and num2")

# Manual Code

num1 = float(input("Enter 1st parameter: "))
num2 = float(input("Enter 2nd parameter: "))
num3 = float(input("Enter 3rd parameter: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)