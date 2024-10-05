def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
a = int(input("enter a"))
b = int(input("enter b"))
print("The sum of",a,'and',b,'is',add(a,b))
print("The sub of",a,'and',b,'is',sub(a,b))
print("The mul of",a,'and',b,'is',mul(a,b))
print("The div of",a,'and',b,'is',div(a,b))