#set in python
print("set:")
thisset={"apple","banana","cherry","apple"} # do not allow duplicate (apple)
tropical = {"pinapple","guva"}
thisset.update(tropical) # add a set (tropical)
thisset.add("papaya") #add papaya
thisset.remove("banana") # remove banana
print(thisset)
print(len(thisset)) #length
print(type(thisset)) # type 
print("-----------------------------------------------")
#A set can contain different data types
print("a set can contain different different data types :")
thislist={True,0,"apple",1,2,False,3} #true and 1 is same value, false and 0 is same value
print(thislist)
print("------------------------------------------------")

#set()constructor
print("set () constructor : ")
thisset = set(("red","blue","green","orange"))
print(thisset)
print("orange" not in thisset) #check "uma" is present in the set false
print(type(thisset))
print("------------------------------------------------")
# access items
# loop (for, in, keyword)
thisset = {"uma","jeya","sara"}
for x in thisset:
  print(thisset)
  print("------------------------------------------------")
  #loop the sets
  my_set={"rose","jasmine","lily","lotus"}
  for x in my_set:
    print(x)
    print("------------------------------------------------")
    #join two sets
set1={"a","b","c"}
set2={"d","e","f"}
myset= set1| set2
print(myset)
print("------------------------------------------------")
#join multiple sets
set1={1,2,3}
set2={"a","b","c"}
set3={"apple","grapes"}
set4= set1.union(set2,set3) #union, multiple sets join
print(set4)