# File: Student.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 10/12/2022
# Description of Program: Makes an object called Student that includes three attributes: name, exam1, and exam2. The program allows users to access and change these attributes and compute student exam averages.

class Student:
    #define Student object and attributes
    def __init__ ( self , name, exam1 = None, exam2 = None) :
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2
    #what will get printed when printing attributes
    def __str__(self):
        return "Student: " + str(self.__name) + "\nExam 1: " + str(self.__exam1) + "\nExam 2: " + str(self.__exam2) 
    #getters and setters to access attributes
    def getName ( self ) :
        return self.__name
    def setName ( self , name ):
        self.__name = name
    def getExam1Grade( self ) :
        return self.__exam1
    def setExam1Grade( self , exam1 ):
        self.__exam1 = int(exam1)
    def getExam2Grade( self ) :
        return self.__exam2
    def setExam2Grade( self , exam2 ):
        self.__exam2 = int(exam2)
    #Averages scores if both are present 
    def getAverage ( self ):
        if self.__exam1 !=None and self.__exam2 !=None:
            return (self.__exam1 + self.__exam2)/2
        else: print("Some exam grades not available.")
    

