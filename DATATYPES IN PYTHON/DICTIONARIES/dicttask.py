#task:1
print("Task : 1")
student={
    "Name" : "Uma",
    "Roll no" : 54,
    "Mark": 455,
    "city":"chenai"
}
Keys=["Name","Roll no","Mark",]
n={y:student[y]for y in Keys}
print(n)
print("_______________________________")
#task : 2
print("Task : 2")
student={
    "name" : "blessy",
    "roll no": 5,
    "mark":456,
    "city":"chennai",
}
deletekey =["mark","city"]
for key in deletekey:
    if key in student:
        del student[key]
print(student)      
print("_______________________________") 
#TASK :3
print("task : 3")
print("Check if a value exists in a dictionary")
my_dict={'a':10,'b':20,'c':30,}
find_value = 20
if find_value in my_dict.values():
    print(f"the value {find_value} exists in the dictionary.")
else:
    print(f"the value {find_value} does not exists in the dictionary")   
print("____________________________________")     
# task :4
print("Task : 4")
print("Rename key of a dictionary")
my_dict={'old_name':'uma'}
my_dict['new name']=my_dict.pop('old_name')
print(my_dict)
print("____________________________________")     
#task : 5
print("Task : 5")
print("Get the key of a minimum value from the following dictionary")
students={'uma':20,'sara':22,'lara':25,'tara':19}
minimum_value = min(students.values())
minimum_keys =[key for key in students if students[key]==minimum_value]
print(minimum_keys)
print("_________________________")
# Task : 6
print("Task : 6")
print("Change value of a key in a nested dictionary : ")
car = {
    "ford": {
        "brand": "ford",
        "model": "Mustang",
        "year": "1964"
    },
    "bmw": {
        "brand": "bmw",
        "model": "a8",
        "year": "2000"
    }
}
x = car["ford"].values()
car["ford"]["year"]=2018
print(x)
print("____________________________________")     
#task:7
print("task : 7")
task=["name","Age","City"]
values =["Uma",19,"chennai"]
dictionaries=dict(zip(task,values))
print(dictionaries)
print("____________________________________")     
#Task : 8
print("task:8")
apple = {"color":"red",}
orange = {"taste":"yummy"}
fruits = apple| orange
print(fruits)
print("____________________________________")     
