# File: PanamaFlag.py
# Student: Diya Sharma 
# UT EID: das5954
# Course Name: CS303E
# 
# Date: 11.18.22
# Description of Program: Uses turtles to draw the panama flag, using functions that define filled in rectangles and stars. 

import turtle

#draw rectangle starting from its top left corner, and fills it in with a color
def DrawRectangle(ttl, color, width, height, x, y):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.color(color)
    ttl.begin_fill()

    for length in [width, height]*2:
        ttl.forward(length)
        ttl.right(90)

    ttl.end_fill()
    ttl.penup()

#draws star from the rightmost inner corner of the star, and fills it in
def DrawStar(ttl, color, length, x,y):
    ttl.penup()
    ttl.goto(x,y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.color(color)
    ttl.begin_fill()
    #five different points
    for turn in range(5):
        ttl.forward(length)
        ttl.right(144)
        ttl.forward(length)
        ttl.right(72-144)

    ttl.end_fill()
    ttl.penup()

#bob defining a turtle class
Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(1)

#turtle coordinates for the flag
DrawRectangle(Bob, '#000000', 1202, 802, -601, 401)
DrawRectangle(Bob, '#F8F8FF', 600, 400, 0, 0)
DrawRectangle(Bob, '#F8F8FF', -600, -400, 0, 0)
DrawRectangle(Bob, '#DC143C', 600, -400, 0, 0)
DrawRectangle(Bob, '#00008B', -600, 400, 0, 0)
DrawStar(Bob, '#00008B', 90, -300, 200)
DrawStar(Bob, '#DC143C', 90, 320, -200)



