# File: Project1.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 10/10/2022
# Description of Program: Grade calculator which allows user to enter a student's name and grades, and it will generate a full grade report based on that information. 


def computeHomeworkAvg(hw1,hw2,hw3):
    #computing avg out of ten then multiplying out of ten to get avg out of 100
    homeAvg = ((hw1+hw2+hw3)/3)*10
    return homeAvg

def computeProjectAvg(p1,p2):
    #already out of 100
    projAvg = (p1+p2)/2
    return projAvg

def computeExamAvg(ex1,ex2):
    #already out of 100
    examAvg = (ex1+ex2)/2
    return examAvg

def wholeAvg(hw1,hw2,hw3,p1,p2,ex1,ex2):
    #using the previous averages and weighting them in final average
    wholeAvg = (0.3*computeHomeworkAvg(hw1,hw2,hw3))+(0.3*computeProjectAvg(p1,p2))+(0.4*computeExamAvg(ex1,ex2))
    return wholeAvg

def avgToLetterGrade(hw1,hw2,hw3,p1,p2,ex1,ex2):
    #decision tree to get final letter grade based on whole numerical average
    wholeAvg = (0.3*computeHomeworkAvg(hw1,hw2,hw3))+(0.3*computeProjectAvg(p1,p2))+(0.4*computeExamAvg(ex1,ex2))
    if wholeAvg >= 90:
        return "A"
    elif wholeAvg >= 80 and wholeAvg < 90:
        return "B"
    elif wholeAvg >= 70 and wholeAvg < 80:
        return "C"
    elif wholeAvg >= 60 and wholeAvg < 70:
        return "D"
    else:
        return "F"

def computeStudentGradeReport(name,hw1,hw2,hw3,p1,p2,ex1,ex2):
    #assigning the previous functions to variables to use in print statements
    hwAvg = (computeHomeworkAvg(hw1,hw2,hw3))
    pAvg = (computeProjectAvg(p1,p2))
    exAvg = (computeExamAvg(ex1,ex2))
    grade = (wholeAvg(hw1,hw2,hw3,p1,p2,ex1,ex2))
    letter = avgToLetterGrade(hw1,hw2,hw3,p1,p2,ex1,ex2)

    #formatting the values in print statements to have only two decimal places
    print("Grade report for:", name)
    print(" Homework average (30% of grade):", format(hwAvg, ".2f"))
    print(" Project average (30% of grade):", format(pAvg, ".2f"))
    print(" Exam average (40% of grade):", format(exAvg, ".2f"))
    print(" Student course average:", format(grade, ".2f")) 
    print(" Course grade (CS303E: Fall, 2022):", letter)


#Score Validation global variables 
HW_ERROR_MESSAGE    = "  Grade must be in range [0..10]. Try again."
PR_EX_ERROR_MESSAGE = "  Grade must be in range [0..100]. Try again."


def main():
    name = input("Enter the student's name (or 'stop'): ")

    #while loop to make the grade calculator loop through the whole class of students
    #while loops after each input to serve as input validators
    while name != "stop":
        print("")
        
        print("HOMEWORKS:")
        hw1 = float(input(" Enter HW1 grade: "))
        while True:
            if hw1<0 or hw1>10:
                print(HW_ERROR_MESSAGE)
                hw1 = float(input(" Enter HW1 grade: "))
            else: break
        hw2 = float(input(" Enter HW2 grade: "))
        while True:
            if hw2<0 or hw2>10:
                print(HW_ERROR_MESSAGE)
                hw2 = float(input(" Enter HW2 grade: "))
            else: break
        hw3 = float(input(" Enter HW3 grade: "))
        while True:
            if hw3<0 or hw3>10:
                print(HW_ERROR_MESSAGE)
                hw3 = float(input(" Enter HW3 grade: "))
            else: break
        print("")
        
        print("PROJECTS:")
        p1 = float(input(" Enter Pr1 grade: "))
        while True:
            if p1<0 or p1>100:
                print(PR_EX_ERROR_MESSAGE)
                p1 = float(input(" Enter Pr1 grade: "))
            else: break
        p2 = float(input(" Enter Pr2 grade: "))
        while True:
            if p2<0 or p2>100:
                print(PR_EX_ERROR_MESSAGE)
                p2 = float(input(" Enter Pr2 grade: "))
            else: break
        print("")
        
        print("EXAMS:")
        ex1 = float(input(" Enter Ex1 grade: "))
        while True:
            if ex1<0 or ex1>100:
                print(PR_EX_ERROR_MESSAGE)
                ex1 = float(input(" Enter Ex1 grade: "))
            else: break
        ex2 = float(input(" Enter Ex2 grade: "))
        while True:
            if ex2<0 or ex2>100:
                print(PR_EX_ERROR_MESSAGE)
                ex2 = float(input(" Enter Ex2 grade: "))
            else: break
        print("")

        computeStudentGradeReport(name,hw1,hw2,hw3,p1,p2,ex1,ex2)
        print("")
        #reinput name to make sure loop is given opportunity to end or user can put in more responses
        name = input("Enter the student's name (or 'stop'): ")
    print("Thanks for using the grade calculator! Goodbye.")

#calling main function with all other function calls inside    
main()




        
