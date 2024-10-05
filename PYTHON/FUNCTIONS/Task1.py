#Task : 1
def student1(name,age):
    print(name,age)
student1("uma",19)
student2 = student1
student2("uma",19)    
# task 2
my_digits = [12, 3, 8, 4, 15, 13, 10, 2, 9, 11]   
list = max(my_digits)  
print("The largest number in the list:", list)  
#task: 3
def largest(a,b,c):
    if (a>b) and (a>c):
        return a 
    elif (b>c):
        return b
    else:
        return c
a = int(input("enter a : ")) 
b = int(input("enter b : "))
c = int(input("enter c : "))   
d = (largest(a,b,c))
print("the largest is : ",d)
#task : 4
def multiply(numbers):
    z = 1
    for x in numbers:
        z *= x
    return z
print(multiply((8, 2, 3, 1, 7))) 
#task : 5
def reverse_string(s):
    return s[::-1]
s = "umasaraswathi"
print(reverse_string(s)) 
#task: 6
# remove duplicate
def list(l):
    x =[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(list([1,2,3,3,3,4,5]))        

