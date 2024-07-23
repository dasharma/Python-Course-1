# File: RecursiveFunctions.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 11/11/2022
# Description of Program: Computes a lot of recursive functions, with the last using a helper function. These functions take various classes of inputs from the user. 

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in 
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Return the sum of the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   if n == 0:
       return 0
   else:
        return n + addToN(n-1)
        
def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   n = str(n) 
   if len(n) == 0:
        return 0
   else:
        return int(n[0]) + int(findSumOfDigits(n[1:]))
    
def integerToBinary( n ):
   """ Given a nonnegative decimal integer n, return the 
   binary representation as a string. """
   remainder = n%2
   n=n//2
   if n == 0:
        return (str(remainder))
   else:
        return integerToBinary(n) + str(remainder)
    
def integerToList( n ):
   """ Given a nonnegative decimal integer, return a list of the 
   digits (as strings). """
   n = str(n)
   digits = [n[0]]
   if len(n) == 1:
       return digits
   else:
       return digits + integerToList(n[1:])

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if len(s) < 1:
       return True
   elif s[0] != s[-1]:
       return False
   else:
       return isPalindrome(s[1:-1]) 

def findFirstUppercase( s ):
   """ Return the first uppercase letter in 
   string s, if any. Return None if there
   is none. """
   if len(s) == 0:
       return None
   elif ord(s[0]) <= 90 and ord(s[0]) >= 65:
       return s[0]
   else: return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex.
   Return the index of the first uppercase letter, 
   beginning at index. Return -1 if there is none."""
   if len(s) == index:
       return -1
   elif ord(s[index]) <= 90 and ord(s[index]) >= 65:
       return index
   else: return findFirstUppercaseIndexHelper(s,index+1)

# The following function is already completed for you. But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in 
   string s, if any. Return -1 if there is none. This one 
   requires a helper function, which is the recursive 
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )
