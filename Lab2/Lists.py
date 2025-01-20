thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Add list item to the last position by .append(value)
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Add list items by to special position by .insert(pos, val)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add elements of a tuple to a list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove the first occurrence of "banana" (первое совпадение)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove by index using .pop(index)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the last item (just .pop())
thislist.pop()

# del - pop's analogy, remove by index 
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# and remove entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# clear() - empties the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# Without list comprehesion
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# With list comprehesion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x.upper() for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]

#------Sort-lists--------
# simple sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# reversed sort
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# or simply
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# customized sort
# The function will return a number that will be used to sort the list (the lowest number first)
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#---------------------
# Copy lists
#1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#3
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#-------------------------
# Join lists
#1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)