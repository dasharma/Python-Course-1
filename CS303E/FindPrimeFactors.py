# File: FindPrimeFactors.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 10.24.2022
# Description of Program: Takes continuous integer inputs and returns a list containing the prime factorization of the numbers. The program is stopped by the number 0 being entered.

import math

def isPrime ( num ):
# Test if a number is prime and return bool true or false
    if ( num < 2 or num % 2 == 0 ):
        return ( num == 2 )
    divisor = 3
    while ( divisor <= math . sqrt ( num )):
        if ( num % divisor == 0 ) :
            return False
        else :
            divisor += 2
    return True

def findNextPrime ( num ):
#Finds the next prime number after the one inputtes
    if ( num < 2 ) :
        return 2
    if ( num % 2 == 0) :
        num -= 1
    guess = num + 2
    while ( not isPrime ( guess )):
        guess += 2
    return guess

def PrimeFactorization(num):
    #Test if number entered is prime already
    if isPrime(num):
        return [num]

   #set the list of factors to the empty list
    else:
        factors = list()
   #set d to 2
        d = 2
    #Find all of the factors and apped them to list
    if num > 1:
        while True:
            if num % d == 0 and num > 1:
                #divide by d until not possible
                factors. append(d)
                num = num // d
            elif num % d != 0 and num > 1:
                #d keeps becoming larger primes 
                nextPrime = findNextPrime(d)
                d = nextPrime
            elif num == 1:
                break
        return factors
    #input is one
    elif num == 1:
        return "1 has no prime factorization."
    #input is negative
    elif num < 0:
        return "Negative integer entered. Try again."


def main():
    print("Find Prime Factors:")
    while True:
        num = int(input("Enter a positive integer (or 0 to stop):"))
        if num != 0:
            print(" The prime factorization of",num, "is:", PrimeFactorization(num))
            print(" ")
        else:
            print("Goodbye!")
            break

main()
                

        
    
