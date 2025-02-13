class Animal:  # Parent class
    def __init__(self, name):
        self.name = name
        print("Animal Class Called")
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Child class inheriting from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent constructor
        self.breed = breed
        print(self.name)

    def speak(self):  # Overriding the parent class method
        print(f"{self.name} barks")

# Creating an object of the child class
dog1 = Dog("Buddy", "Golden Retriever")
dog1.speak()  # Output: Buddy barks

