# Manual Code
for i in range(50):
    if i == 25:
        break
    print(i)

# Own Code
# Print prime numbers
# Python program to display all the prime numbers within an interval

lower = 0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)