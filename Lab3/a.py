class MyClass:
    a = 5
    
    def __init__(self, b):
        self.b = b
    
    def print_a():
        print(a)
    def print_b(self):
        print(self.b)
        
print(MyClass.a)        
myclass = MyClass(10)

print()