#bitwise operators
print("Bitwise operators :")
#parenthesis operator
print("parenthesis operator")
print((6 + 3) - (6+3))
#exponentiation
print("exponentiation")
print(100 - 3**3)
#unary plus
print("unary plus")
print(100 + ~3)
#unary minus
print("unary minus")
print(100 - ~3)
#multipication and add
print(100 + 5 * 3)

#task 1 :
# decimal value convert to binary value
decimal_number = 42
binary_number = bin(decimal_number)[2:]
print(binary_number)

#task 2 :
# binary value convert to decimal value
binary_number = '101010'
decimal_number = int(binary_number,2)
print(decimal_number)
print("_____________________________________________") 
#task : 3
a = input('binary :')
b = input('binary :')
c = bin(int(a,2) + int(b,2))
d = int (c,2)
print("binary c:",c)
print("binary d:",d)
