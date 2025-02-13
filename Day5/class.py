# # # syntax

# # class Student: # age = 18 
# #     age = 18 #static variable

# #     # Student(){
        
# #     # }
# #     #self yeuta variable 
# #     def __init__(self, name, level, address): # constructor
# #         print("Constructor called ")
# #         self.student_name = name
# #         self.student_level = level
# #         self.student_address = address
        
# #     def displayStudentName(self):
# #         print(self.student_name)

# #     def displayStudentDetails(self):
# #         print(self.student_name)
# #         print(self.student_address)
# #         print(self.student_level)
# #         print(self.age)

        
# # first_student = Student("Ishan","Bsc Hons", "Itahari")
# # second_student = Student("Bardan","XI", "Ktm")
# # # Student.__init__
# # print(first_student.displayStudentDetails())
# # print(second_student.displayStudentDetails())
# # # print(first_student.age)
# # # print(second_student.age)
# # # Student.add()

# class Student:
#     #static variable
#     school_name = "Digital Pathshala"
#     #id, #name
#     def __init__(self,id,name):
#         self.id = id #instance variable
#         self.name = name #instance variable
        
#     #instance method
#     def displayStudentDetail(self):
#         print(self.school_name)
#         # pass
#         print("hello")
#     def helloHi():
#         print("hello")
# student_one = Student(100,"Manish")
# student_one.displayStudentDetail()

# Dog  => Child Class
# Animal => Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    #instance method
    def displayAnimalname(self):
        print(self.name)
    # def run animal
    
    # def eatfood

#super = Parent
class Dog(Animal):# Dog inherit Animal
    # def __init__(self, name):
    #     self.name = name
    # #instance method
    # def displayAnimalname(self):
    #     print(self.name)
    def __init__(self):#automatically called while creating object 
        super().displayAnimalname()
    #instance method
    def speak(self,name):
        super().__init__(name)
        print(f"{self.name} barks")

# dog_one = Dog("Dog 1") #creation object 
dog_2 = Dog("Dog 2") #name = Dog 2

dog_2.displayAnimalname()
dog_2.speak("name")