# File: MyStringFunctions.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 10/17/2022
# Description of Program: A group of functions designed to help students understand how to index and append strings.

def myAppend( s, ch ):
    # returns old string plus new character
    return s + ch

def myCount( s, ch ):
    # count how many times ch is in s 
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count

def myExtend( s1, s2 ):
    # add s2 at end of s1
    return s1 + s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    if s=="":
        print( "Empty string: no min value")
        return None
    else:
        letter = str
        storage = ord(s[1])
        for c in s:
            ordinal = ord(c)
            if ordinal < storage:
                storage = ordinal
                letter = c
        return letter
        
def myInsert( s, i, ch ):
    # insert ch in the ith position of s
    if i>len(s):
        print("Invalid index")
    else:
        part1 = s[:i]
        part2 = s[i:]
        whole = part1 + ch + part2
        return whole

def myPop( s, i ):
    #return a new string that is like s but with the ith element removed;
    #return the value that was removed.
    if i >= len(s):
        print("Invalid index")
        return s, None
    else:
        part1 = s[:i]
        part2 = s[i+1:]
        return (part1 + part2, s[i])
    

def myFind( s, ch ):
    # Return the index of the first occurrence of ch 
    if ch not in s:
        return -1
    else:
        for i in range(len(s)):
            if s[i]==ch:
                return i
                break

def myRFind( s, ch ):
    # Return the index of the last occurrence of ch in s. Return -1 if ch does not occur in s.
    if ch not in s:
        return -1
    else:
        count = 0
        for i in range(len(s)):
            if s[i]==ch:
                count = i
        return count
                
                
def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    if ch not in s:
        return s
    else:
        for i in range(len(s)):
            if s[i]==ch:
                part1 = s[:i]
                part2 = s[i+1:]
                whole = part1 + part2
                break
        return whole

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    if ch not in s:
        return s
    else:
        whole = ""
        for i in s:
            #count = count + 1
            if i != ch:
                whole = whole + i
        return whole


def myReverse( s ):
    # Return a new string like reverse of s
    reverse = ""
    for x in range(1,len(s)+1):
        reverse = reverse + s[-x]
    return reverse
        
        
