# File: WordleAssistant.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 11/05/2022
# Description of Program: Basically a some helper functions forr a game of wordle, filtering a large wordlist to find wors that match certain conditions.

def createWordlist(filename): 
    wordlist=[]
    infile = open ( filename , "r" )
    word = infile.readline().strip()
    while word:
        #sets can't contain duplicate letters so it would automatically delete any repeats
        if len(word)==5 and word[-1]!="s" and len(set(word)) == len(word):
            wordlist.append(word)
        word = infile.readline().strip()
    infile.close()
    return (wordlist, len(wordlist)) 
        
def containsAll(wordlist, include):
    letters = set(include)
    words = set(wordlist) 
    matchList = set()
    noMatchList = set()
    for word in words:
        for x in letters:
            word = str(word)
            if x not in word:
                noMatchList.add(word)
    #compare the two sets and make a list of the differences
    matchList = words.difference(noMatchList)
    return (matchList)

def containsNone(wordlist, exclude):
    letters = set(exclude)
    words = set(wordlist) 
    matchList = set()
    noMatchList = set()
    for word in words:
        for x in letters:
            word = str(word)
            if x in word:
                matchList.add(word)
    #compare the two sets and make a list of the differences
    noMatchList = words.difference(matchList)
    return (noMatchList)


def containsAtPositions(wordlist, posInfo):
    #posInfo tells the position of each character
    posSet = []
    count = 0
    for word in wordlist:
        for letter in word:
            if letter in posInfo:
                if word.index(letter) == posInfo.get(letter):
                    count = count+1
        if count == len(posInfo):
            posSet.append(word)
        count = 0
    return set(posSet)

def getPossibleWords(wordlist, posInfo, include, exclude):
    inList = containsAll(wordlist, include)
    exList = containsNone(wordlist, exclude)
    total = inList.intersection(exList)
    return(containsAtPositions(total, posInfo))

                    
                    
            
    
    
        

    
