thisdict={
    "name" : "uma",
    "age"  : 20,# Dictionaries cannot have two items with the same key:
    "age"  : 19,
    "gender" : "female",
    "favcolor": ["red","blue","pink"]#The values in dictionary items can be of any data type [list]
}
thisdict["name"] = "saraswathi" # change the value
thisdict.update({"eyecolor":"black"}) # add the value
thisdict.pop("gender") # remove gender value
thisdict.popitem() # the last value is remove`  .0`
print(thisdict)
print(len(thisdict)) # dict length
print(thisdict["name"])
print(type(thisdict))
