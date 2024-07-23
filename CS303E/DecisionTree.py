# File: DecisionTree.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 09/19/2022
# Description of Program: This program accepts different characteristics of a person and outputs whether people will buy a computer.


#assigning different inputs as variables
age = int(input("Please enter person's age: "))
income = input("Person's income (High, Medium, Low): ")
student = input("Is this person a student (Yes or No)? ")
credit = input("Does this person have good credit (Yes or No)? ")

#initializing the variable buy as an empty string variable
buy: str

#If statements from decision tree
if student == "Yes" and age>40 and credit == "Yes":
    buy = "no"
elif student == "Yes":
    buy = "yes"
elif age <= 30:
    buy = "no"
elif credit == "No":
    buy = "yes"
elif age <= 40:
    buy = "yes"
else: buy = "no"

#print statements based on buy variable 
if buy == "yes":
    print("This person will purchase a computer.")
else:
    print("This person will not purchase a computer.")
          

          
