# File: Project3.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 11.30.22
# Description of Program: This program defines a way to encode and decode different text files. It validates all inputs and allows users to set the ciphers used to encode and decode the texts. 

import random
import os
import sys

LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):
   key = key.lower()
   return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )

def makeRandomKey():
   lst = list( LCLETTERS )
   random.shuffle( lst )
   return ''.join( lst )

class SubstitutionCipher:
   #this defines a class that allows te user to interact with the program by changing the ciphers and inputting different text files
   def __init__(self, key = makeRandomKey()):
       self.key = key.lower()

   
   def getKey(self):
       return self.key

 
   def setKey(self, key):
          if isLegalKey(key):
             self.key = key.lower()
          else:
             print("Illegal key entered. Try again!")


   
   def encryptFile(self, inFile, outFile):
      #the next two functions look through a text file line by line and convert the characters by using the conversion dictionary
       with open(inFile, "r") as f:
           with open(outFile, "w") as f1:
               for line in f:
                   for ch in line:
                       if ch.isalpha():
                           if ch.isupper(): 
                              f1.write(self.key[LCLETTERS.index(ch.lower())].upper())
                           else: f1.write(self.key[LCLETTERS.index(ch.lower())])
                       else:
                           f1.write(ch)

   
   def decryptFile(self, inFile, outFile):
       with open(inFile, "r") as f:
           with open(outFile, "w") as f1:
               for line in f:
                   for ch in line:
                       if ch.isalpha():
                           if ch.isupper(): 
                              f1.write(LCLETTERS[self.key.index(ch.lower())].upper())
                           else: f1.write(LCLETTERS[self.key.index(ch.lower())])
                       else:
                           f1.write(ch)

   
   def makeConversionDictionary(self, key1, key2):
      #dictionary that allows the program to search for the letter positions to make it possible to code and encode the text files
       dict = {}
       for i in range(len(key1)):
           dict[key1[i]] = key2[i]
       return dict
   
   

def main():
   cipher = SubstitutionCipher()
   while True:
      
       cmd = input("Please enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ").lower()
       
       if cmd == "quit":
           print("Thanks for visiting!")
           print(" ")
           break
         
       elif cmd == "getkey":
           print("   Current cipher key:", cipher.getKey())
           print(" ")
           
       elif cmd == "changekey":
           while True:
              cmd1 = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
              if cmd1 == "quit":
                 print(" ")
                 break
              elif cmd1 == "random":
                 cipher.setKey(makeRandomKey())
                 print("      New cipher key: ", cipher.getKey())
                 print(" ")
                 break
              else:
                 if isLegalKey(cmd1):
                    cipher.setKey(cmd1)
                    print("      New cipher key: ", cipher.getKey())
                    print(" ")
                    break
                 else:
                    print("      Illegal key entered. Try again!")
                     
                  
       elif cmd == "encryptfile":
          #this part converts the filename, adding an extension, also processes it whether there is a .txt or not 
           inFile = input("   Enter a filename: ")
           if not os.path.isfile(inFile):
               print("File does not exist.")
           else:
               extension = "-Enc"                  
               if inFile.endswith(".txt"):
                  outFile = inFile[:-4] + extension + ".txt"
               else:
                  outFile = inFile + extension
               print("The encrypted output filename is", outFile)
               cipher.encryptFile(inFile, outFile)

               
       elif cmd == "decryptfile":
           inFile = input("   Enter a filename: ")
           if not os.path.isfile(inFile):
               print("File does not exist.")
               print(" ")
           else:
               extension = "-Dec"                  
               if inFile.endswith(".txt"):
                  outFile = inFile[:-4] + extension + ".txt"
               else:
                  outFile = inFile + extension
               print("The decrypted output filename is", outFile)
               cipher.decryptFile(inFile, outFile)
               print(" ")
       else:
           print("   Command not recognized. Try again!")
           print(" ")


main()
