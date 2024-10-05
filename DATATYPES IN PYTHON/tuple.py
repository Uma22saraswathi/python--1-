#tuple allow duplicate values
thistuple = ("banana","grapes","cherry","apple","orange","banana","cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
print(thistuple[2])
print(thistuple[:4])
print(thistuple[4:])
print("_______________________")

#change tuple values
x = ("red","blue","green","yellow")
y = list(x)
y[3]="pink"
x=tuple(y)
print(x)
print("_______________________")

#add tuple values
thistuple=("tomato","potato","brinjal")
y = ("orange",)
thistuple += y
print(thistuple)
print(type(thistuple))
print("_______________________")

#packing tuple
names = ("uma","sara","lara","thara")
print(names)
print("_______________________")
#unpacking a tuples
numbers = ("one","two","three")
(uma,lara,sara) = numbers
print(lara)
print("_______________________")
