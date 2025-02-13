class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        print(f"Student {self.name} has been created.")


s1 = Student("Ishan", 20)  # Output: Student Ishan has been created.
