def painter():
    print("painting")
painter()
print("________________________")
 #add
print("add")
def add():
    a = int(input("enter a :"))
    b = int(input("enter b :"))
    print(a+b)
add() 
print("________________________")
#sub
print("sub")
def sub():
    a = int(input("enter a :"))
    b = int(input("enter b :"))  
    print(a-b) 
sub()   
print("________________________")
 #parameters function  
print("parameters function : ")
def painter(msg):
    print("Message:",msg)
painter("paint my house")

def student(msg):
   print("Message :",msg)  
student("tommarrow start the puplic exam")  
print("________________________")
 #find even or odd
print("Find Even Or Odd : ")
def findevenorodd(b):
    if(b%2==0):
        print("Even")
    else:
        print("Odd")    
a = int(input("enter a value : "))
findevenorodd(a)   
print("________________________")    

print("student pass or fail : ")
def passorfail(b):
    if(b>=35):
        print("Pass")
    else:
        print("Fail")
a = int(input("Enter The Student Mark : "))
passorfail(a)            
print("________________________")   
# range() function method
print("range () method : 1 : ")
def printrange():
    for i in range (1,11):
        print(i)
printrange()   
print("________________________")        
  # another method  
print("range () method : 2 : ") 
def printrange1(r1,r2):
    for i in range(r1,r2):
        print(i)
a = int(input("Enter a : "))  
b = int(input("Enter b : "))      
printrange1(a,b) 
print("________________________")           

a = [1, 2, 3]
b = [3, 2, 3]

print(a == b)  # Output: True (same value)
print(a is b)  # Output: False (different objects in memory)
