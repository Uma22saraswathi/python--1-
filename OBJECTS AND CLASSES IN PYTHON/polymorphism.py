#polymorphism refers to methods/functions/operators with the same name that can be executed on many objects or classes.
#polymorphism
def add(a,b,c=0):
    print(a+b+c)
add(1,2)
add(1,2,3)
print("________________________________")
class animal():
    def sound(self):
        print("animal makes sound") 
class dog(animal):  
   def sound(self):
       print("dog barks")   
class bird(animal):
    def sound(self):
        print("bird's sing")       
a1=animal()
a1.sound()
d1 = dog()
d1.sound() 
brd = bird()
brd.sound()          