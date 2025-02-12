# DRY
def take_input():
    return int(input("Enter a number: "))
def calculate(a,b):
    sum = a + b
    difference = a - b
    product = a * b
    return sum, difference , product , #n
a = take_input()
b = take_input()
calcualtion = calculate(a,b) # product, #n (sum, difference, product)
print(calcualtion)
print(type(calcualtion))

