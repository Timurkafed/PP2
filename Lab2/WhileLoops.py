i = 1
while i < 6:
  print(i)
  i += 1
  
# break - stops the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue - stops the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Else in While Condition
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

