# File: FunctionExamples.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
# 
# Date Created: 09/30/2022
# Description of Program: Twelve functions that take different numerical inputs and complete mathematical operations on them.


import math

# sums three numbers

def sum3Numbers (x, y, z):
    return x + y + z

# multiplies three numbers

def multiply3Numbers( x, y, z ):
    return x * y * z

# sums up to three numbers

def sumUpTo3Numbers (x, y = 0, z = 0):
    return x + y + z

# multiplies up to  three numbers

def multiplyUpTo3Numbers (x, y = 1, z = 1):
    return x * y * z

# prints two numbrs in order

def printInOrder( x, y ):
    if x<y:
        print(x,y)
    elif x>y:
        print(y,x)

# area of square

def areaOfSquare( side ):
    if side<0:
        print("Negative value entered")
    else:
        return side*side

# perimeter of a square

def perimeterOfSquare( side ):
    if side<0:
        print("Negative value entered")
    else:
        return side*4

# area of a circle

def areaOfCircle( radius ):
    if radius<0:
        print("Negative value entered")
    else:
        return math.pi*radius**2

# circumference of a circle

def circumferenceOfCircle( radius ):
    if radius<0:
        print("Negative value entered")
    else:
        return 2*math.pi*radius

# figuring out if both numbers entered are factors of the third one

def bothFactors( d1, d2, x ):
    if x%d1==0 and x%d2==0:
        return 'True'
    else:
        return 'False'

# use above functions to print area and perimeter of both a circle and square

def squareAndCircle( x ):
    print()
    print("Circle with radius", x, "has:")
    print(" Area:",areaOfCircle(x))
    print(" Circumference:",circumferenceOfCircle(x))
    print("Square with side", x, "has:")
    print(" Area:",areaOfSquare(x))
    print(" Perimeter:",perimeterOfSquare(x))
    print()

# computes factorials

def factorial( n ):
    num = int(1)
    if n<0:
        print("Input must be positive.")
        return none 
    else:
        for x in range(1,n+1):
            num = x*num
        return(num)
    
    
