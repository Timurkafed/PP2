'''
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
solvedLH = solve(heads, legs)
print("Rabbits:", solvedLH[0], ", Chickens:", solvedLH[1])

print("\n---------4---------")

'''
def filter_prime(numbers):
    numstr = ""
    array_numbers = []
    prime_numbers = []
    for num in numbers:
        if num != " ":
            numstr += num
        else:
            array_numbers.append(int(numstr))
            numstr = ""
    array_numbers.append(int(numstr))
    for num in array_numbers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            prime_numbers.append(num)
    print (prime_numbers)
    return prime_numbers
numbers = input("Numbers separated by spaces: ")
                    
print( *filter_prime(numbers), sep = ", ")
