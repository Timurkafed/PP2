# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Changable. Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Create and print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Dictionaries cannot have two items with the same key. Rewrites to latest value.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# String, int, boolean, and list data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Using the dict() constructor method to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# Get the value of the "model" key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# or
x = thisdict.get("model")

# .keys() - returns a list of all the keys in the dictionary
x = thisdict.keys()

# .values() - returns a list of all the values in the dictionary
x = thisdict.values()

# .items() - returns each item in a dictionary, as tuples in a list
x = thisdict.items() # output: dict_items([('key1', 'value1'), ('key2', 'value2')])


# Check if key exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#--------------Changing-Items----------------
#Simple example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# .update({key:value}) is used to update items. Either adds a new one if there is none or changes the existing one
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# or, simply, we can use that previous way
thisdict["color"] = "red"


# Removing items by key using .pop(key) method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# .popitem() removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# del keyword removes the item with the specified key too
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# or, we can use it for deleting whole dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The .clear() method empties the dictionary

#-------------Loops-------------
# Print all key names in the dictionary
for x in thisdict:
  print(x)
# or use .keys():
for x in thisdict.keys():
  print(x)
  
  
# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])
# or use .values():
for x in thisdict.values():
  print(x)
  
# Loop through both keys and values, by using the .items()
for x, y in thisdict.items():
  print(x, y)
  

#---------Copy-Dict----------
# .copy() - make a copy of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function .dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


#-----------Nested-Dictionaries--------------
# A dictionary can contain dictionaries, this is called nested dictionaries
# Create a dictionary that contain three dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child2"]["name"]) # Print the name of child 2

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
    
