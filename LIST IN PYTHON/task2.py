mylist=list(range(1,11))
even_number = []
for x in mylist[:]:
    if x % 2 == 0:
        even_number.append(x)
    else:
        mylist.remove(x)
print(mylist)
print(even_number)

     