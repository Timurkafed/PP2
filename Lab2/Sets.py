# Set items are unchangeable, but you can remove items and add new items.
# Sets are unordered, so you cannot be sure in which order the items will appear.

# Sets like lists but th cannot have two items with the same value (Duplicate values will be ignored)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# The values True and 1/False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, False, 0, 2}
print(thisset) # {False, True, 2, 'banana', 'apple', 'cherry'}

#---------Access-Items-------------
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the "in" keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
# Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#-------------Add-Items---------------
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# .update() - for adding items from another set into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# P.S.: The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#-------Remove-Items----------
# use .remove(item) or .discard(item) for removing item
'''If the item to remove does not exist, 
remove() will raise an error,
discard() will NOT raise an error.
'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove a random item by using the pop() method
# (Sets are unordered, so when using the pop() method, you do not know which item that gets removed.)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# del, clear(), loops are used the same as lists

#------------Join-Sets-----------------
# .union() - returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# or just
set4 = set1 | set2 # | = .union()
print(set3)
print(set4)

# Join multiple sets with the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
# P.S.: The  | operator only allows you to join sets with sets

# .update() method inserts all items from one set into another.
# .update() do the same as .union(), but .update() changes the original set, and does not return a new set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


# Intersection
# .intersection() returns only duplicates between sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) # "apple"
# or just &
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 # & operator only allows you to join sets with sets
print(set3)

# .intersection_update() - объединение intersection and update (returns only duplicates and changes the original set)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The values True and 1\False and 0 are considered the same value
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)


# Difference
# .difference() - returns a new set that will contain only the items from the first set that are not present in the second set
# сет1 - сет2 = сет1 но без элементов из сет2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
#or just -
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 # - operator only allows you to join sets with sets
print(set3)

# .difference_update() - ну тут понятно

# .symmetric_difference() - keeps only the elements that are NOT present in both sets
# сет1 ^ сет2 = объединение двух сетов кроме дубликатов, появляющиеся при объединении
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
# or just ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 # ^ operator only allows you to join sets with sets
print(set3)

# .symmetric_difference_update() - everything is clear here

