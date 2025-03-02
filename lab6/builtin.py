#1
list = [2, 3, 4]

multiplied = eval('*'.join(map(str, list)))
print(multiplied)

#2
text = 'HeLlO WoRlD!'

upper = sum(letter.isupper() for letter in text)
lower = sum(letter.islower() for letter in text)

print("Uppercases:", str(upper) +'.', "Lowercases:", lower)

#3 
word = "Palilap".lower()
if word == ''.join(reversed(word)):
    print("Eto palindrom")
else:
    print("Eto ne palindrom")
    
#4
import math
import datetime
def squareRoot(num, milsek):
    delta = datetime.timedelta(milliseconds=milsek)
    end = datetime.datetime.now() + delta
    while datetime.datetime.now() < end:
        pass
    return(math.sqrt(num))

a = 25100
b = 2123
print("Square root of",a, "after", b, "miliseconds is", squareRoot(a,b))


#5
tuple1 = (True, True, True, 1)  
tuple2 = (True, 0, True, True)  

print(all(tuple1))
print(all(tuple2))