# Final Project
# CS 111, Reckinger
# Eduardo Morales
# November 20nth
# [Final Project Name]
# The message that we wanted to share with this project was simple.
# Take your time.


# MODULES
import turtle
import random
import math

# FUNCTIONS

# read the lines from the text file that I made that has each line for the project


def get_lines(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    return lines

# this function stalls / delays what is happening on the screen for a given amount of time


def stall(speed, distance):
    tt = turtle.Turtle()
    tt.hideturtle()
    tt.penup()
    tt.speed(speed)
    tt.forward(distance)

# this shows the user chose the wrong choice!


def redo(x, y):
    xmark.hideturtle()
    checkmark.hideturtle()
    text.clear()
    screen.bgcolor('skyblue')
    text.write('To Bad! Redo the drawing!', False,
               align='center', font=('Arial', 20))
    stall(1, 500)

   # this is the function that starts the movie, starting with scene1


def scene1(x, y):
    checkmark.hideturtle()
    xmark.hideturtle()
    text.clear()
    text.write('Buckle up then!', False, align='center', font=('Arial', 20))
    stall(1, 500)
    screen.bgcolor('skyblue')
    text.clear()
    screen.tracer(0)
    draw_floor('brown')
    draw_fence()
    draw_flower('yellow', 'green', -134, -250)
    draw_flower('red', 'skyblue', -50, -250)
    draw_flower('thistle', 'lavender', -244, -250)
    draw_outside_house()
    screen.tracer(1)
    scene2()


def scene2():
    stall(5, 1000)
    screen.tracer(0)
    screen.clear()
    draw.clear()
    screen.bgcolor('black')
    text.penup()
    text.color('white')
    text.goto(0, 250)
    text.write('Scene 2', False, align='center', font=('Arial', 20))
    stall(1, 700)
    screen.clear()
    text.clear()
    screen.bgcolor('#F0E68C')
    draw_floor('black')
    draw_exit()
    setup_desk()

# this function draws a floor


def draw_floor(color):
    draw.showturtle()
    draw.penup()
    draw.goto(-600, -300)
    draw.setheading(90)
    draw.pencolor('black')
    draw.fillcolor('#8B4513')
    draw.pendown()
    draw.begin_fill()
    for i in range(2):
        draw.right(90)
        draw.forward(1200)
        draw.right(90)
        draw.forward(50)
    draw.end_fill()
    draw.penup()
    draw.hideturtle()

# this function draws a fence


def draw_fence():
    draw.goto(-600, -300)
    draw.pencolor('black')
    draw.fillcolor('#B8860B')
    draw.pendown()
    for i in range(12):
        draw.setheading(90)
        draw.begin_fill()
        draw.forward(400)
        draw.right(90)
        draw.forward(100)
        draw.right(90)
        draw.forward(400)
        draw.right(90)
        draw.forward(100)
        draw.end_fill()
        draw.setheading(0)
        draw.forward(100)
    draw.penup()

# this function draws a flower


def draw_flower(color1, color2, x, y):
    draw.goto(x, y)
    draw.pendown()
    draw.setheading(270)
    draw.pencolor('black')
    draw.fillcolor('black')
    draw.begin_fill()
    for i in range(2):
        draw.forward(50)
        draw.right(90)
        draw.forward(2)
        draw.right(90)
    draw.end_fill()
    draw.begin_fill()
    for i in range(2):
        draw.forward(50)
        draw.left(90)
        draw.forward(2)
        draw.left(90)
    draw.end_fill()

    draw.goto(x, y)
    draw.pencolor(color2)
    draw.fillcolor(color1)
    draw.pendown()
    for i in range(13):
        draw.begin_fill()
        draw.circle(40, 70)
        draw.left(110)
        draw.circle(40, 70)
        draw.goto(x, y)
        draw.end_fill()
    draw.fillcolor(color2)
    draw.pencolor(color1)
    for i in range(9):
        draw.begin_fill()
        draw.circle(20, 45)
        draw.left(55)
        draw.circle(20, 45)
        draw.goto(x, y)
        draw.end_fill()
    draw.penup()


def draw_outside_house():
    draw.goto(-300, -300)
    draw.pendown()
    draw.pencolor('black')
    draw.fillcolor('#6495ED')
    draw.setheading(90)
    draw.begin_fill()
    draw.forward(500)
    draw.setheading(135)
    draw.goto(-600, 400)
    draw.setheading(270)
    draw.forward(700)
    draw.setheading(0)
    draw.forward(300)
    draw.end_fill()
    draw.penup()
    draw.goto(-550, 150)
    draw.pendown()
    draw.setheading(90)
    draw.fillcolor('#778899')
    draw.begin_fill()
    for i in range(4):
        draw.right(90)
        draw.forward(200)
    draw.end_fill()


def rectangle(draw, width, height, color):
    draw.fillcolor(color)
    draw.begin_fill()
    draw.forward(width)
    draw.left(90)
    draw.forward(height)
    draw.left(90)
    draw.forward(width)
    draw.left(90)
    draw.forward(height)
    draw.left(90)
    draw.end_fill()


def triangle(draw, length, color):
    draw.fillcolor(color)
    draw.begin_fill()
    draw.forward(length)
    draw.left(135)
    draw.forward(length / math.sqrt(2))
    draw.left(90)
    draw.forward(length / math.sqrt(2))
    draw.left(135)
    draw.end_fill()


def draw_tree(x, y):
    draw.goto(x, y)
    draw.fillcolor()
    for i in range(4):
        draw.begin_fill()
        draw.forward(100)
        draw.left(90)
        draw.endfill()
    for i in range(5):
        draw.begin_fill()
        draw.forward(100)
        draw.cirlce(30, 55)


def draw_exit():
    draw.penup()
    draw.goto(200, 200)
    draw.pencolor('red')
    draw.pendown()
    draw.fillcolor('white')
    draw.setheading(90)
    draw.begin_fill()
    for i in range(2):
        draw.forward(100)
        draw.right(90)
        draw.forward(200)
        draw.right(90)
    draw.end_fill()
    text.goto(300, 212)
    text.color('red')
    text.write('Exit', False, align='center', font=('Arial', 50))
    draw.penup()
    draw.goto(500, 200)
    draw.pendown()
    draw.pencolor('black')
    draw.fillcolor('brown')
    draw.setheading(180)
    draw.begin_fill()
    for i in range(2):
        draw.forward(400)
        draw.left(90)
        draw.forward(500)
        draw.left(90)
    draw.end_fill()
    draw.shape('circle')
    draw.color('black')
    draw.penup()
    draw.goto(450, 0)
    draw.stamp()
    draw.penup()


def setup_desk():
    desk.goto(-500, -100)
    desk.stamp()
    desk.hideturtle()
    flipped_desk.goto(500, -100)
    flipped_desk.stamp()
    flipped_desk.hideturtle()
    mainsitting.goto(-400, -100)
    mainsitting.showturtle()
    mainsitting.pendown()
    other_guy.goto(400, -100)
    other_guy.showturtle()
    other_guy.pendown()
    other_guy.stamp()


# MAIN

list = get_lines('lines.txt')

# define basic first screen, etc
screen = turtle.getscreen()
screen.bgcolor('red')
screen.tracer(1)

# define basic the text turtle, which we will use to write, etc
text = turtle.Turtle()
text.penup()
text.hideturtle()
text.goto(0, 200)
text.write(list[0], False, align='center', font=('Arial', 20))

# define the checkmark turle
checkmark = turtle.Turtle()
turtle.addshape('checkmark.gif')
checkmark.shape('checkmark.gif')
checkmark.penup()
checkmark.goto(-250, 75)

# define the xmark turtle
xmark = turtle.Turtle()
turtle.addshape('xmark.gif')
xmark.shape('xmark.gif')
xmark.penup()
xmark.goto(250, 75)
xmark.onclick(redo)

# define the drawing turtle
draw = turtle.Turtle()
draw.hideturtle()
draw.speed('fastest')
draw.penup()

tree = turtle.Turtle()
tree.color('black')
tree.shape('turtle')
tree.speed('fastest')
tree.penup()
draw.goto(100, -130)
tree.pendown()
rectangle(tree, 20, 40, 'brown')
tree.penup()
tree.goto(65, -90)
tree.pendown()
triangle(tree, 90, 'green')
tree.penup()
tree.goto(70, -45)
tree.pendown()
triangle(tree, 80, 'green')
tree.penup()
tree.goto()

# define the turtle object that is at the window
windowguy = turtle.Turtle()
turtle.addshape('windowstick.gif')
windowguy.shape('windowstick.gif')
windowguy.hideturtle()
windowguy.penup()

# define the turtle object that swings
swingguy = turtle.Turtle()
turtle.addshape('swingguy.gif')
swingguy.shape('swingguy.gif')
swingguy.hideturtle()
swingguy.penup()

# define the turtle object that is a desk
turtle.addshape('desk.gif')
desk = turtle.Turtle(shape='desk.gif')
desk.hideturtle()
desk.penup()

# define the turtle object that is our main character in scene 2
turtle.addshape('desksitting.gif')
mainsitting = turtle.Turtle(shape='desksitting.gif')
mainsitting.hideturtle()
mainsitting.penup()

# define sitting other guy
turtle.addshape('other_guy.gif')
other_guy = turtle.Turtle(shape='other_guy.gif')
other_guy.hideturtle()
other_guy.penup()

# define the flipped desk for scene 2
turtle.addshape('flipped_desk.gif')
flipped_desk = turtle.Turtle(shape='flipped_desk.gif')
flipped_desk.hideturtle()
flipped_desk.penup()

# add an event to the checkmark
checkmark.onclick(scene1)
turtle.mainloop()  # uncomment once you start doing turtle drawing
screen.mainloop()
