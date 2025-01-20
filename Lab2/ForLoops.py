# for loop - executes a set of statements, once for each item in a list, tuple, set etc.
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# break - stops the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# continue - stops the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
# RANGE
# for i in range(toNum)
for x in range(6):
  print(x)

# for i in range(from, to)
for x in range(2, 6):
  print(x)

# for i in range(from, to, step)
for x in range(2, 30, 3):
  print(x)

# Else in For Loop
for x in range(6):
  print(x)
else: # P.S.: the else block will NOT be executed if the loop is stopped by a break statement.
  print("Finally finished!")

# Nested Loops - is a loop inside a loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
# PASS
for x in [0, 1, 2]:
  pass