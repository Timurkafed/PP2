thistuple = ("apple",)
print(type(thistuple)) # output: <class 'tuple'>

# NOT a tuple (it's str)
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")

# Change tuple vlaue
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add items
# 1. Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# !!!Tuples are unchangeable, so you cannot remove items from it.
# But we can convert the tuple into a list, remove the value we want, and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Although, we can completely delete the whole tuple by "del"
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#--------------
# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterik *
# Используется если в анпакинге участвует меньше переменных чем элементов в тюпле. * перед переменной забирает на себя оставшиеся элементы с тюпла, но сам становится списком.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red) 
'''output:
apple
banana
['cherry', 'strawberry', 'raspberry']
'''
# ex. 2
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
'''output:
apple
['mango', 'papaya', 'pineapple']
cherry
'''
# В остальном тюплы работают так же как и списки
