# File: Handicap.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 09/12/2022
# Description of Program: This program takes in three game scores from bowlers and outputs a report of the average of the three scores, and the handicap that player would receive in the game. 

#Collect name of bowler
print("")
name = input("Enter bowler's name: ")

#Collect each of the scores

score1 = int(input("Enter Game 1: "))
score2 = int(input("Enter Game 2: "))
score3 = int(input("Enter Game 3: "))

#Calculate gaming average then handicap
avg = int((score1 + score2 + score3) / 3)
handicap = int((200 - avg) * 0.8)

print("")
print("Handicap report for", name+":")

print(" ",name+"\'s", "average is:", avg)
print(" ",name+"\'s", "handicap is:", handicap)

print("")
print("It's time to Bowl!")
print("")

      
