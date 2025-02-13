class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):  # Instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
s1 = Student("Ishan", 20)
s1.greet()  # Output: Hello, my name is Ishan and I am 20 years old.
