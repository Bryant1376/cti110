# Keyon Bryant
# 4/5/24
# P4LAB1B
# Description: Drawing Initials

import turtle

# Set up the turtle
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Initials Drawing")
t = turtle.Turtle()

# Set the pen color and size
pen_color = "blue"
pen_size = 4
t.color(pen_color)
t.pensize(pen_size)

# Function to draw the initial "K"
def draw_initial_K():
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.right(90)
    t.forward(200)
    t.backward(100)
    t.left(45)
    t.forward(100)
    t.backward(100)
    t.left(80)
    t.forward(100)
    t.penup()

    
# Move to the right
    t.goto(0,0)
    t.pendown()

# Function to draw the initial "B"
def draw_initial_B():
    t.left(55)
    t.forward(-300)
    t.right(90)
    t.circle(75, 180)
    t.left(180)
    t.circle(75, 180)
    t.penup()
  

# Draw the initials
draw_initial_K()
draw_initial_B()

# Hide the turtle and display the drawing
t.hideturtle()
screen.mainloop()

