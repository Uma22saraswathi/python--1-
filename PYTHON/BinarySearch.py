# Binary search
l=(input("enter the list of numbers : "))
mylist = [int(x) for x in l.split(',')]
mylist.sort()
print(mylist)
s =int(input("enter the element"))
start = 0
end = len(mylist)-1

while(start<=end):
    mid=(start+end)//2
    if s==mylist[mid]:
        print(mid)
        print(end)
        print(start)
        print("element found at",mid+1)
        break
    
    elif (s < mylist[mid]):
        print("mid ",mid)
        print("end",end)
        print(start)
        end = mid-1
        print(mid)
        print(end)
        print(start)
    else:
        print(mid)
        print(end)
        print(start)
        start=mid+1
        print(mid)
        print(end)
        print(start)
else:
    print("not found")            


