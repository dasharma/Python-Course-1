# File: MinMax.py
# Student: Diya Sharma
# UT EID: das5954
# Course Name: CS303E
#
# Date: September 23, 2022
# Description: Program asks for any number of integer inputs and prints the maximum and minimum values once it is prompted to stop

num = input("Enter an integer or 'stop' to end: ")

# Prints statement if 'stop' is the first input
if num == "stop":
    print("You didn't enter any numbers")

else:
    # Stores maximum and minimum values
    xNum = int(num)
    nNum = int(num)

    # Creates loop for an arbitrary amount of inputs
    while True:
        num = input("Enter an integer or 'stop' to end: ")
        
        # Keeps track of the current maximum and minimum values
        if num != "stop":
            if int(num) < nNum:
                nNum = int(num)
            elif int(num) > xNum:
                xNum = int(num)

        # Ends the loop once prompted
        elif num == "stop":
            break

    # Prints maximum and minimum values
    print("The maximum is", xNum)
    print("The minimum is", nNum)

