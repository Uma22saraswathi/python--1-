mylist = ["apple","orange","banana","mango","kiwi","lemon"]
mylist[1:2] = ["cherry","watermelon"]
print(mylist)
print(len(mylist))#list length
print(mylist[2])
print(mylist[0:2])
print(mylist[:4])
print(mylist[2:])

#list items data types
list1 = ["apple","orange","cherry"] #string
list2 = [10,20,30,40] #int
list3 = [True,False,False] #boolean
print(list1)
print(len(list1))

print(list2)
print(list3)
#a list can contain different data types
list4 = ["apple",10,True] # string,int,bool
print(list4)
print(type(list4))#type()
#list()constructor
thislist = list(("uma","sara","lara"))# two double round brackets(())
mylist = ["sameera","reha","maya"]
thislist.extend(mylist)#extend
thislist.insert(1,"divya")#insert name
thislist.append(1 )#append
thislist.pop(3)
print(thislist)
print(type(thislist))  
# sort the list alphabetically
xlist =["uma","anu","brindha","chithra","divya"] 
xlist.sort()

print(xlist)                                     
#Sort the list numerically
listy = [1,2,3,4,5,6,100,18,20,50]
listy.sort()
print(listy)
#sort the list descending
listz =["apple","ball","cat","dog","zebra","elephant"]
listz.sort(reverse = True)
print(listz)
#copy the list
alist = ["riya","roriri","nexgen"]
blist = alist[:] #slice operator
print(blist)