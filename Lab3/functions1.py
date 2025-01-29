print("---------1---------")
def GramToOunces(gram):
    return gram / 28.3495231
gram = float(input("Grams: "))
print("Ounces:", round(GramToOunces(gram), 7))

print("\n---------2---------")
def FarhToCel(F):
    return (5 / 9)*(F - 32)
F = float(input("Degree Fahrenheit: "))
print("Degree Celsius:", FarhToCel(F))

print("\n---------3---------")
def solve(numheads, numlegs):
    rabbits = numlegs//2-numheads
    chickens = numheads - rabbits
    return rabbits, chickens

legs = 94
heads = 35
print("Rabbits:", solve(heads, legs)[0], ", Chickens:", solve(heads, legs)[1])

