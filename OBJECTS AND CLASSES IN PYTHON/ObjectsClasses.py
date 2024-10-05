#class and object 
class Demo:
    print("class method")
    a = 10
    print(a)
    b = 20
obj = Demo 
print(obj.b)  
print("_________________________________")
#function in class 
class demo1:
    print("function method")
    d = 20
    def example (self,a,b):
        c = a+b+self.d
        print(c)
obj = demo1()    
obj.example(20,10)
print("_________________________________")
#init function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("uma",20)
print(p1.name)
print(p1.age)        
print("_________________________________")
#types of class methods
class laptop():
    chargertype = "C type"
    def __init__(self):
        self.brand =""
        self.price = 34
    def setprice(self,price):
        self.price = price
    def getprice (self):
        print(self.price) 
    @classmethod
    def changechargertype(cls):
        cls.changechargertype = "B type"
        print(" charger type changed to B")

hp = laptop()   
hp.setprice (20000)
hp.getprice()
laptop.changechargertype()
