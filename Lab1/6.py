x = 5
y = "John"
print(type(x))
print(type(y))
#--------------------
myVariableName = "John"
#--------------------
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#--------------------
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#--------------------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#--------------------
