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

print("\n---------5---------")
from itertools import permutations

def print_permutations():
    s = input()
    t = permutations(s)
    for i in t:
        print(''.join(i))
print_permutations()

print("\n---------6---------")

def reversed(s):
    words = s.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

s = input()
reversed(s)


print("\n---------7---------")

def has_33(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == 3:
            if nums[i+1] == 3:
                return True
        i += 1
    return False

numbers = input()
nums = numbers.split()
nums = [int(num) for num in nums]
print(has_33(nums))


print("\n---------8---------")

def spy_game(nums):
    s = ''
    for i in nums:
        s += i
    if '007' in s:
        return True
    return False

numbers = input()
nums = numbers.split()
print(spy_game(nums))


print("\n---------9---------")

def radius(r):
    sphere = 4/3*3.14*r**3
    return sphere 

r = int(input())
print(radius(r))


print("\n---------10---------")

def unique(l):
    list1 = []
    i = 0
    while i < len(l):
        t = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t = False
            j += 1
        if t:
            list1.append(l[i])
        i += 1
    return list1

l = input()
elements = l.split()
list1 = unique(elements)
print(list1)


print("\n---------11---------")

def palindrome(s):
    i = 0
    j = len(s)-1
    while i < len(s)/2:
        if s[i] != s[j]:
            return 'No'
        i+=1
        j-=1
    return 'palindrome'

s = input()
print(palindrome(s))


print("\n---------12---------")

def histogram(t):
    i = 0
    while i < len(t):
        j = 0
        while j < t[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

t = input()
t = t.split()
t = [int(num) for num in t]
histogram(t)


print("\n---------13---------")

import random

def find(num, t):
    t += 1
    num2 = int(input('Take a guess.\n'))
    if num2 == num:
        print(f'Good job, KBTU! You guessed my number in {t} guesses!')
        return
    print('\nYour guess is too low.')
    return find(num, t)

name = input('Hello! What is your name?\n')
num = random.randint(1, 20)
t = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find(num, t)


