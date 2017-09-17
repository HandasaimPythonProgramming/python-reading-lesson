from math import sqrt # this line allows us to use the sqrt function in line 4

def pythagoras(a, b):
    return sqrt(a**2 + b**2)

print("Please enter a number:")
number1 = int(input())
print("Please enter another number:")
number2 = int(input())
print("Result:", pythagoras(number1, number2))