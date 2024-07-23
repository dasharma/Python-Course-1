# File: ComparingLinearBinarySearch.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 10.28.2022
# Description of Program: Provides functions that do linear and binary searches of datasets.
#   these searches happen an n number of times and the number of iterations to find a certain value are returned.

import math
import random

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

def nSearches(lst, n):
    #for any number of searches, return average numbers of times function reiterates
    probes = list()
    for x in range (0,n):
        probes.append((linearSearch(lst, random.randint(0, 999)))+1)
    probeAvg = sum(probes) / len(probes)
    return probeAvg 

def nBinarySearches(lst, n):
    #for any number of searches, return average numbers of times function reiterates
    probes = list()
    for x in range (0,n):
        index,count = binarySearch(lst, random.randint(0, 999))
        probes.append(count)
    probeAvg = sum(probes)/len(probes)
    return probeAvg

def main():
    #generate list in order and a random list
    search = list(range(0, 999))
    randSearch = list(range(0, 999))
    random.shuffle(randSearch)

    #linear searches in order of increasing iterations
    print("Linear search:")
    print(" Tests: 10", "      Average probes:", nSearches(randSearch, 10))
    print(" Tests: 100", "     Average probes:", nSearches(randSearch, 100))
    print(" Tests: 1000", "    Average probes:", nSearches(randSearch, 1000))
    print(" Tests: 10000", "   Average probes:", nSearches(randSearch, 10000))
    print(" Tests: 100000", "  Average probes:", nSearches(randSearch, 100000))

    #storing probe average for 1000 times 
    binary1000 = nBinarySearches(search, 1000)
    print("Binary search:")
    print(" Average number of probes:", binary1000)
    print(" log2(1000):", math.log2(1000))
    print("  Differs from log2(1000) by:", (math.log2(1000) - binary1000))
        
main()
