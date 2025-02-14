# 1.Write a function that takes two numbers as input and returns their sum.

def sum(a,b):
    return a+b
print(sum(5,8))


#METHOD: 2
def sum(a,b):
    print(a+b)
sum(5,8)



# 2.Write a function that takes a number as input and returns its square.

def square(a):
    return a**2
print(square(10))


#METHOD:2
def square(a):
    print(a**2)
square(10)



# 3.Write a function that checks if a number is even or odd.

def odd_or_even(a):
    if a%2==0:
        print('The number is Even.')
    else:
        print('The number is Odd.')
odd_or_even(9)



# 4.Write a function that returns the largest of three numbers.

def greatest_number(a,b,c):
    if b<a>c:
        return(f'The greatest number is {a}.')
    elif a<b>c:
        return(f'The greatest number is {b}.')
    else:
        return(f'The greatest number is {c}.')
print(greatest_number(98,9,730))


#METHOD:2
def greatest_number(a,b,c):
    if b<a>c:
        print(f'The greatest number is {a}.')
    elif a<b>c:
        print(f'The greatest number is {b}.')
    else:
        print(f'The greatest number is {c}.')
greatest_number(98,9,730)



# 5.Write a function that takes a name and prints "Hello, [name]".

def name():
    n=input('Enter your name:')
    print(f'Hello {n}')
name()



# 6.Write a function that calculates the factorial of a given number.

def factorial(f):
    for i in range(1,f):
        f*=i
    print(f'The factorial of the given numbner is {f}.')
factorial(3)



# 7.Write a function that takes a list of numbers and returns the sum of all the numbers.

def sum_of_numbers_in_list():
    s=0
    list=[2,3,4,5,6]
    for i in list:
        s+=i
    return(f'The sum of the numbers in the given list is {s}.')
print(sum_of_numbers_in_list())


#METHOD:2
def sum_of_numbers_in_list():
    s=0
    list=[2,3,4,5,6]
    for i in list:
        s+=i
    print(f'The sum of the numbers in the given list is {s}.')
sum_of_numbers_in_list()