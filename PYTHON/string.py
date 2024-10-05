# python string 
print("Hello")
print('hi')
a = ("uma")
print(a)
print("------------------------------")
#multiline string
b = """ Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)
print("------------------------------")
#reverse string
name = "umasaraswathi"
print(name[::-1])
print("------------------------------")
#slice string
print("slice string")
b = "Hello,World"
print(b[0])
print(b[2:5])
print(b[:5])
print(b[5:])
print(b[-2])
print(b[-4])
print(b[:-4])
print("------------------------------")
#modify strings
name = "umasaraswathi"
print(name.upper())

names = "BLESSY"
print(names.lower())
z = "  uma  "
print(z.strip())#remove space
print(z.replace("u","U"))#replace
print("------------------------------")
#concatenation
a = "roriri"
b = "software"
c = a + " " + b # space between roriri " " software
print(c)
print("------------------------------")
#format string
age = 19
txt = f"My name is uma, i am {age}"
print(txt)
print("------------------------------")
#placeholders and modifier
price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)
print("------------------------------")
#escape charecters
txt = "we are \"vikings\" from the north"
print(txt)
print("------------------------------")
