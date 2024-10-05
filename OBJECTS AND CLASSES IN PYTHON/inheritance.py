#inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
print("single and multiple inheritance : ")
class dad():
    def phone(self):
        print("dad's phone")
class mom():# multiple inheritance
    def car(self):
        print("mom's car")      
class son(dad,mom):
    def laptop(self):
        print("Son's laptop") 
ram=son()  
ram.laptop()
ram.phone() 
ram.car()# multiple inheritance
print("________________________________")
#multi level inheritance
print(" multi level inheritance : ")
class grandpa():
    def money(self):
        print("grandpa's money")
class dad(grandpa):
    def phone(self):
        print("dad's phone")    
class son(dad):
    def laptop(self):
        print("son's laptop")
ram=son()   
ram.laptop()
ram.phone()
ram.money()
sam=dad()
sam.money()
print("___________________________________")
#hierarchical inheritance
print("Hierarchical inheritance : ")
class dad(): # base class
    def money(self):
        print("dad's money")
class son1(dad):
    pass # empty class
class son2(dad):
    pass
class son3(dad):
    pass
s2 = son2()   
s2.money() 
s1 = son1()
s1.money()
s3 = son3()
s3.money()
print("__________________________________")
#hybrid inheritance
print("Hybrid inheritance : ")
class dad():
    def money(self):
        print("dad's money")
class land():
    def important(self):
        print("important land")    
class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass  
s2 = son2()   
s2.money()
s1 = son1()
s1.important()   
print("___________________________________")
