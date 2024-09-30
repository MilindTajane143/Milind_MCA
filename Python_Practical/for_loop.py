# Manual Code

names = ['Rajesh', 'Disha','Milind']
for n in names:
    print(n)



# Own Code
n = int(input("Enter the number of elements: "))  
my_list = []  

for i in range(n):  
    element = input("Enter element {}: ".format(i + 1))  
    my_list.append(element)

print("List:", my_list)
