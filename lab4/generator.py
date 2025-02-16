print("-----------1-----------")
def square_of_number(N):
    for i in range(N+1):
        yield i**2

num = int(input("Number: "))
gen = square_of_number(num)

for square in gen:
    print(square, end=" ")
    
print("\n-----------2-----------")
def even_nums(n):
    for i in range(0, n+1):
        if i%2 == 0:
            yield i
            
num = int(input("Number: "))
gen = even_nums(num)

print(", ".join(map(str, gen)))
    
print("\n-----------3-----------")
def task3(n):
    for i in range(0, n+1):
        if i%3 == 0 or i%4 == 0:
            yield i
            
num = int(input("Number: "))
gen = task3(num)

print(", ".join(map(str, gen)))

print("\n-----------4-----------")
def squares(start, finish):
    for i in range(start, finish+1):
        yield i**2
            
start = int(input("Start: "))
finish = int(input("Finish: "))

gen = squares(start, finish)
print(", ".join(map(str, gen)))

for i in range(start, finish+1):
    if i !=finish:
        print(i**2, end=", ")
    else:
        print(i**2)

print("\n-----------5-----------")
def tozero(N):
    for i in range(N+1,-1,-1):
        yield i

num = int(input("From num: "))
gen = tozero(num)

for square in gen:
    print(", ".join(map(str, gen)))