import math

print("--------------1--------------")
degree = float(input("Degree: "))
print(round(math.radians(degree), 6))

print("\n--------------2--------------")
def trapezoidal_area(base1, base2, height):
    area = 0.5 * math.fsum([base1, base2]) * height
    return area

base1 = int(input("Base 1: "))
base2 = int(input("Base 2: "))
height = int(input("Height: "))
print(trapezoidal_area(base1, base2, height))

print("\n--------------3--------------")
def area_of_regular_polygon(n, length):
    area = n*pow(length,2)/4*math.tan(math.pi/n)
    return round(area)

n = int(input('number of sides: '))
length = float(input('length of each side: '))
print('Area:', area_of_regular_polygon(n, length))

print("\n--------------4--------------")
def area_parallelogram(base, height):
    area = math.prod([base, height])
    return area

base = float(input('Base: '))
height = float(input('Height: '))
print('Area:', area_parallelogram(base,height))
