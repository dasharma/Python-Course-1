import random
import os
import sys

LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey( key ):

   return ( len(key) == 26 and all( [ ch in key for ch in LCLETTERS ] ) )
def makeRandomKey():
   lst = list( LCLETTERS )
   random.shuffle( lst )
   return ''.join( lst )

class SubstitutionCipher:
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
       code = dict()
       final = str()
       for i in range(len(LCLETTERS)): 
           code[LCLETTERS[i]] = self.key[i]
       f = open(inFile, "r")
       f1 = open(outFile, "w")
       lines_f = f.readlines()
       for line in lines_f:
           for ch in line:
               if ch.isalpha():
                   if ch.isupper():
                       ch = ch.lower()
                       enc = code[ch].upper()
                   else:
                       enc = code[ch]
               else: enc = ch
           final = final + enc
       f1.write(final)
       
   
   def decryptFile(self, inFile, outFile):
       with open(inFile, "r") as f:
           with open(outFile, "w") as f1:
               for line in f:
                   for ch in line:
                       if ch.isalpha():
                           f1.write(LCLETTERS[self.key.index(ch.lower())])
                       else:
                           f1.write(ch)

   
   def makeConversionDictionary(self, key1, key2):
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
           break
       elif cmd == "getkey":
           print("Current cipher key:", cipher.getKey())
       elif cmd == "changekey":
           while True:
               cmd1 = input("Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
               if cmd1 == "quit":
                   break
               elif cmd1 == "random":
                   cipher.setKey(makeRandomKey())
                   print("New cipher key: ", cipher.getKey())
                   break
               else:
                   cipher.setKey(cmd1)
                   break
       elif cmd == "encryptfile":
           inFile = input("Please enter the name of the file to encrypt: ")
           if not os.path.isfile(inFile):
               print("File does not exist.")
           else:
               extension = "-Enc"
               if inFile.endswith(".txt"):
                   outFilename = inFile[:-4] + extension + ".txt"
                   print("The encrypted file will be called", outFilename)
                   cipher.encryptFile(inFile, outFilename)
                   
               else:
                   outFilename = inFile + extension
                   print("The encrypted file will be called", outFilename)
                   cipher.encryptFile(inFile, outFilename)
                   

       elif cmd == "decryptfile":
           inFile = input("Please enter the name of the file to decrypt: ")
           if not os.path.isfile(inFile):
               print("File does not exist.")
           else:
               outFile = inFile + "-Dec"
               print("The decrypted file will be called", outFile)
               cipher.decryptFile(inFile, outFile)
               file_contents = outFile.read()
               print(file_contents)
       else:
           print("Command not recognized. Try again!")


main()
