# #Task 1
# # calculator

def calculator():
	a = int(input("Enter a : "))
	b = int(input("Enter b : "))
	c = input('operators: +,-,*,/ : ')
	if c == '+':
		print("The sum is :",a+b)
	elif c== '-':
		print("The sub is :", a-b)
	elif c== '*':
		print("The multipication is :",a*c)
	elif c=='/':
		print("The division is :",a/b)
	else:
		print("thanks")	
calculator()
#Task 2
def list_sum(num_List):
	if len(num_List) == 1:
		return num_List[0]
	else:
		return num_List[0] + list_sum(num_List[1:])
	print(list_sum([2, 4, 5, 6, 7]))

#Task : 3
#program to find factorial of given number 
# def factorial(n): 
# 	fact=1
# 	while n>0:
# 		fact=fact*n
# 		n=n-1
# 	return fact  	
# print("Factorial of",factorial(n=int(input("Number : ")))); 


