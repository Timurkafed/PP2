a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# Short Hand If
if a > b: print("a is greater than b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B") # This technique is known as Ternary Operators, or Conditional Expressions.

# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# NOT
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if - when if statements inside if statements
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
# pass - we can use it if we have if statements, but don't have anuthing in body of these if st-s
# Просто пустой if
a = 33
b = 200

if b > a:
  pass

