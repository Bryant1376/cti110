# Keyon Bryant
# 4/5/24
# P4LAB1A
# Description: Creating shapes
 

import turtle

# Set up the turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Square and Triangle Drawing")
t = turtle.Turtle()

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Move the turtle to the starting position for drawing the square
t.penup()
t.goto(-150, 0)
t.pendown()

# Draw the square
draw_square()

# Move the turtle to the starting position for drawing the triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw the triangle
draw_triangle()

# Hide the turtle and display the drawing
t.hideturtle()
screen.mainloop()







