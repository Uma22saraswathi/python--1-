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