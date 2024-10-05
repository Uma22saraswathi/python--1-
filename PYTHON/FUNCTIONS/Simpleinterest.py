pr = int(input("enter principal : "))
rate = int(input("enter rate : "))
months = int(input("enter months : "))
si = (pr*rate*months)/100
amount = pr+si
print("simple interest : ", si)
print("amount payable : ",amount)