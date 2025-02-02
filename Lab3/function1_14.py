from functions1 import FarhToCel, solve, GramToOunces

F = float(input("Degree Fahrenheit: "))
print("Degree Celsius:", FarhToCel(F))

legs = 94
heads = 35
solvedLH = solve(heads, legs)
print("\nRabbits:", solvedLH[0], ", Chickens:", solvedLH[1])

gram = float(input("Grams: "))
print("Ounces:", round(GramToOunces(gram), 7))