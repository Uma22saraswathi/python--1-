#task 1
l=[1,4,5,6,3,7,9,2]
print("list has the items :",l)
s = int(input("Enter a number to search for : "))
for i in range(len(l)):
    if l[i] == s:
        print("item is found in the given position",i)
        break
else:
    print("item is not found in the list")
    
#task 2 
    
input_values = input("Enter a list of numbers separated by commas: ")
# Convert the string input to a list of integers
mylist = [int(x) for x in input_values.split(',')]
print("List has the items:", mylist)

searchitem = int(input("Enter a number to search for: "))

for i in range(len(mylist)):
    if mylist[i] == searchitem:
        print("Item is found in the given position", i)
        break
else:
    print("Item is not found in the list")
