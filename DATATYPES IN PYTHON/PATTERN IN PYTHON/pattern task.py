n = int(input("enter the value of number"))
for i in range(n):
    print(i,end=" ")
print()
print("________________________________________________")
    
n = int(input("enter a value :"))
for i in range(n,6,-5):
     for j in range(i):
        print("*",end=" ")
     print(i)

    #right triangle
print("right triangle")
r = int(input("enter the value :"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

r = int(input("enter the value :"))
for i in range(1,r+1):    
    for j in range(1,i+1):
        print(i,end=" ")
    print()
    # pyramid triangle
r = int(input("enter a number"))   
space= r-1
for i in range(0,r):
    for j in range(0,space):
        print(" ", end= "")
    space = space -1
    for k in range(0,i+1):
      print(k, end=" ")
    print()
 #inverted right triangle 
print("inverted right triangle ")
n = int(input("enter a number of r :"))  
for row in range(n,0,-1):
    for column in range (1,row+1):
        print(column,end=" ")
    print()
   #
n = int(input("enter the value"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print() 



