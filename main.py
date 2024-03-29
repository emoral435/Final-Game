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

# this reads the file lines.txt and returns the lines back into the format of a list


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
    draw_tree()
    screen.tracer(1)
    scene2()

# this is the scene 2 of the movie


def scene2():
    stall(5, 1000)
    tree.clear()
    draw.clear()
    screen.bgcolor('black')
    text.penup()
    text.color('white')
    text.goto(0, 250)
    text.write('Scene 2', False, align='center', font=('Arial', 20))
    stall(1, 700)
    screen.tracer(0)
    text.clear()
    screen.bgcolor('#F0E68C')
    # draw_floor('black')
    # draw_exit()
    # setup_desk()
    mainsitting.showturtle()
    # define sitting other guy
    turtle.addshape('other_guy.gif')
    other_guy = turtle.Turtle()
    other_guy.shape('other_guy.gif')
    other_guy.hideturtle()
    other_guy.penup()
    other_guy.goto(400, -130)
    # flipped other guy turtle!
    turtle.addshape('flipped_other.gif')
    flipped_other = turtle.Turtle(shape='flipped_other.gif')
    flipped_other.hideturtle()
    flipped_other.penup()
    flipped_other.goto(400, -130)
    other_guy.showturtle()
    screen.tracer(1)
    # stall(1,100)
    # text_bubble('black', 'white', 400, 100, -350, 200)
    # textbub.goto(-150, 230)
    # textbub.write('Library', False, align='center', font=('Arial', 30))
    # stall(1,500)
    # textbub.clear()
    # stall(1, 200)
    # text_bubble('black', 'white', 400, 100, -350, 200)
    # textbub.goto(-150, 230)
    # textbub.write('Furious Typing...', False, align='center', font=('Arial', 30))
    # stall(1,500)
    # textbub.clear()
    # library_interaction(other_guy, flipped_other)
    # stall(1,400)
    scene3(other_guy)


def scene3(other_guy):
    draw.clear()
    mainsitting.hideturtle()
    text.clear()
    other_guy.hideturtle()
    flipped_desk.clear()
    desk.clear()
    screen.bgcolor('black')
    text.penup()
    text.color('white')
    text.goto(0, 250)
    text.write('Scene 3', False, align='center', font=('Arial', 20))
    stall(1, 700)
    # screen.tracer(0)
    # text.clear()
    # draw_box()
    # create the chair turtle
    turtle.addshape('chair.gif')
    chair = turtle.Turtle(shape='chair.gif')
    chair.penup()
    chair.hideturtle()
    # create the main guy turtle where he is reading
    turtle.addshape('mainguy.gif')
    reading = turtle.Turtle(shape='mainguy.gif')
    reading.penup()
    reading.hideturtle()
    # create the standing turtle
    turtle.addshape('standing.gif')
    standing = turtle.Turtle(shape='standing.gif')
    standing.penup()
    standing.hideturtle()
    # create phone turtle to indicate to open the terminal!
    turtle.addshape('phone.gif')
    phone = turtle.Turtle(shape='phone.gif')
    phone.hideturtle()
    phone.penup()
    # time = random.randint(1,3)
    # if time == 1:
    #   screen.bgcolor('skyblue')
    #   draw_window('skyblue')
    #   message = 'Home - Day'
    # elif time == 2:
    #   screen.bgcolor('#502161')
    #   draw_window('#502161')
    #   message = 'Home - Sunset'
    # else:
    #   screen.bgcolor('#f6652c')
    #   draw_window('#f6652c')
    #   message = 'Home - Night'
    # draw_floor('#2d180c')
    # draw_bed()
    # flipped_desk.goto(500, -100)
    # flipped_desk.stamp()
    # chair.goto(100, -170)
    # chair.stamp()
    # screen.tracer(1)
    # reading.goto(220, -140)
    # standing.goto(220, -140)
    # reading.showturtle()
    # stall(1,100)
    # text_bubble('black', 'white', 400, 100, 0, 200)
    # textbub.goto(200, 230)
    # textbub.write(message, False, align='center', font=('Arial', 30))
    # stall(1,500)
    # textbub.clear()
    # stall(1, 200)
    # text_bubble('black', 'white', 400, 100, 0, 200)
    # textbub.goto(220, 230)
    # textbub.write('Ahhh, I should rest..', False, align='center', font=('Arial', 24))
    # stall(1,700)
    # textbub.clear()
    # reading.hideturtle()
    # standing.showturtle()
    # stall(1,300)
    # standing.goto(-200, -140)
    # stall(1, 200)
    # text_bubble('black', 'white', 600, 100, -75, 200)
    # textbub.goto(220, 230)
    # textbub.write('Should I give the studying a break?', False, align='center', font=('Arial', 24))
    # phone.goto(200,0)
    # stall(1,400)
    # phone.stamp()
    # stall(1,700)
    # answer = turtle.textinput('Should he rest?', 'Enter yes or no')
    # answer.lower()
    # stall(1,200)
    # textbub.clear()
    # phone.clear()
    # if (answer == 'yes') or (answer == 'y'):
    #   rest(standing, reading)
    # else:
    #   grind(standing, reading)
    # text_bubble('black', 'white', 600, 100, -75, 200)
    # textbub.goto(220, 230)
    # textbub.write('what the heck is bubble sort...', False, align='center', font=('Arial', 16))
    scene4(chair, reading)


def scene4(chair, reading):
    stall(1, 700)
    screen.clear()
    flipped_desk.clear()
    draw.clear()
    chair.clear()
    reading.hideturtle()
    textbub.clear()
    screen.bgcolor('black')
    text.penup()
    text.color('white')
    text.goto(0, 250)
    text.write('Scene 4', False, align='center', font=('Arial', 20))
    stall(1, 700)
    screen.tracer(0)
    text.clear()
    # define the house turtle
    turtle.addshape('house.gif')
    house = turtle.Turtle(shape='house.gif')
    house.hideturtle()
    house.penup()
    screen.bgcolor('skyblue')
    draw_floor('#3e931f')
    # define the old man character turtle
    turtle.addshape('old.gif')
    oldman = turtle.Turtle(shape='old.gif')
    oldman.hideturtle()
    oldman.penup()
    oldman.goto(-500, -160)
    oldman.showturtle()
    house.goto(730, -45)
    house.showturtle()
    house.stamp()
    draw.penup()
    draw.goto(-800, 400)
    draw.fillcolor('yellow')
    draw.begin_fill()
    draw.circle(100)
    draw.end_fill()
    text_bubble('black', 'white', 600, 100, -450, 200)
    textbub.goto(-140, 180)
    textbub.write(list[15], False, align='center', font=('Arial', 30))
    stall(1, 700)
    oldman.speed(1)
    oldman.goto(-80, -160)
    textbub.clear()
    text_bubble('black', 'white', 600, 100, -450, 200)
    textbub.goto(-160, 180)
    textbub.write(list[16], False, align='center', font=('Arial', 30))
    stall(1, 700)
    text_bubble('black', 'white', 950, 100, -750, 50)
    textbub.goto(-260, 40)
    textbub.write(list[17], False, align='center', font=('Arial', 30))
    stall(1, 600)
    textbub.goto(-260, 0)
    textbub.write(list[18], False, align='center', font=('Arial', 30))
    stall(1, 600)
    text_bubble('black', 'white', 200, 70, -380, -50)
    textbub.goto(-260, -105)
    textbub.write(list[19], False, align='center', font=('Arial', 35))
    stall(1, 700)
    textbub.clear()
    draw.clear()
    oldman.hideturtle()
    house.clear()
    house.hideturtle()
    screen.bgcolor('black')
    text.penup()
    text.color('white')
    text.goto(0, 150)
    text.write(list[20], False, align='center', font=('Arial', 50))
    stall(1, 1000)
    text.clear()
    text.goto(0, 0)
    text.write('The End', False, align='center', font=('Arial', 80))
    stall(1, 300)
    answer = turtle.textinput('Rewatch?', 'Enter yes or no')
    answer.lower()
    stall(1, 400)
    if (answer == 'yes') or (answer == 'y'):
        scene1(0, 0)
    else:
        pass


def grind(standing, reading):
    text_bubble('black', 'white', 800, 100, -250, 200)
    textbub.goto(150, 230)
    textbub.write('Your right, I should keep on studying.',
                  False, align='center', font=('Arial', 24))
    stall(1, 700)
    textbub.clear()
    text_bubble('black', 'white', 800, 100, -250, 200)
    textbub.goto(160, 250)
    textbub.write('What would I even do anyways?', False,
                  align='center', font=('Arial', 24))
    textbub.goto(160, 170)
    textbub.write(list[14], False, align='center', font=('Arial', 24))
    stall(1, 1000)
    textbub.clear()
    standing.goto(220, -140)
    stall(1, 350)
    standing.hideturtle()
    reading.showturtle()
    stall(1, 300)


def rest(standing, reading):
    text_bubble('black', 'white', 800, 100, -250, 200)
    textbub.goto(150, 230)
    textbub.write('I know you said yes, and the bed looks nice, but...',
                  False, align='center', font=('Arial', 24))
    stall(1, 700)
    textbub.clear()
    text_bubble('black', 'white', 800, 100, -250, 200)
    textbub.goto(160, 220)
    textbub.write(list[13], False, align='center', font=('Arial', 24))
    textbub.goto(160, 170)
    textbub.write(list[14], False, align='center', font=('Arial', 24))
    stall(1, 600)
    textbub.clear()
    standing.goto(220, -140)
    stall(1, 350)
    standing.hideturtle()
    reading.showturtle()
    stall(1, 300)


def draw_window(color):
    draw.penup()
    draw.goto(-500, 100)
    draw.fillcolor(color)
    draw.width(10)
    draw.pencolor('black')
    draw.pendown()
    draw.setheading(90)
    draw.begin_fill()
    for i in range(2):
        draw.forward(200)
        draw.right(90)
        draw.forward(200)
        draw.right(90)
    draw.end_fill()
    draw.penup()
    draw.goto(-400, 100)
    draw.pendown()
    draw.forward(200)
    draw.setheading(0)
    draw.penup()
    draw.goto(-500, 200)
    draw.pendown()
    draw.forward(200)
    draw.penup()
    draw.width(1)


def draw_box():
    draw.penup()
    draw.goto(-600, -300)
    draw.setheading(90)
    draw.fillcolor('#c6ab85')
    draw.pendown()
    draw.pencolor('black')
    draw.begin_fill()
    for i in range(2):
        draw.forward(700)
        draw.right(90)
        draw.forward(1200)
        draw.right(90)
    draw.end_fill()
    draw.penup()


# this function draws a floor
def draw_floor(color):
    draw.showturtle()
    draw.penup()
    draw.goto(-600, -300)
    draw.setheading(90)
    draw.pencolor('black')
    draw.fillcolor(color)
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
    flipped_desk.goto(500, -100)
    flipped_desk.stamp()


def draw_tree():
    tree.penup()
    tree.goto(450, -300)
    tree.pendown()
    rectangle(tree, 50, 100, 'brown')
    tree.penup()
    tree.goto(320, -220)
    tree.pendown()
    triangle(tree, 300, 'green')
    tree.penup()
    tree.goto(340, -100)
    tree.pendown()
    triangle(tree, 250, 'green')
    tree.penup()
    tree.goto(350, 20)
    tree.pendown()
    triangle(tree, 230, 'green')
    tree.penup()
    tree.goto(360, 100)
    tree.pendown()
    triangle(tree, 200, 'green')
    tree.penup()


def text_bubble(pencolor, fillcolor, length, width, x, y):
    textbub.speed('fastest')
    textbub.penup()
    textbub.goto(x, y)
    textbub.pencolor(pencolor)
    textbub.fillcolor(fillcolor)
    textbub.begin_fill()
    textbub.pendown()
    textbub.setheading(90)
    screen.tracer(1)
    for i in range(2):
        textbub.forward(width)
        textbub.right(90)
        textbub.forward(length)
        textbub.right(90)
    textbub.end_fill()
    textbub.penup()


def library_interaction(other_guy, flipped_other):
    textbub.penup()
    textbub.goto(330, 50)
    textbub.pendown()
    textbub.goto(300, 100)
    text_bubble('black', 'white', 100, 50, 200, 100)
    textbub.goto(250, 100)
    textbub.color('#d87c08')
    textbub.write('!', False, align='center', font=('Arial', 30))
    stall(1, 300)
    textbub.clear()
    stall(1, 150)
    other_guy.hideturtle()
    flipped_other.showturtle()
    flipped_other.speed(1)
    flipped_other.goto(-100, -130)
    textbub.goto(-20, 20)
    textbub.pencolor('black')
    textbub.pendown()
    textbub.goto(-20, 250)
    textbub.penup()
    text_bubble('black', 'white', 1000, 100, -500, 250)
    textbub.goto(0, 280)
    textbub.write(list[7], False, align='center', font=('Arial', 18))
    stall(1, 600)
    textbub.goto(0, 240)
    textbub.write(list[8], False, align='center', font=('Arial', 18))
    stall(1, 700)
    textbub.clear()
    textbub.goto(-400, 135)
    textbub.pendown()
    textbub.goto(0, 250)
    textbub.penup()
    text_bubble('white', 'black', 1000, 100, -500, 250)
    textbub.goto(0, 260)
    textbub.color('white')
    textbub.write(list[9], False, align='center', font=('Arial', 18))
    stall(1, 600)
    textbub.goto(-20, 20)
    textbub.pendown()
    textbub.goto(-20, 100)
    textbub.penup()
    textbub.color('black')
    text_bubble('black', 'white', 700, 100, -345, 100)
    textbub.goto(10, 110)
    textbub.write(list[10], False, align='center', font=('Arial', 18))
    stall(1, 700)
    textbub.clear()
    stall(1, 300)
    other_guy.goto(-100, -130)
    flipped_other.hideturtle()
    other_guy.showturtle()
    other_guy.speed(1)
    other_guy.goto(400, -130)


def draw_bed():
    draw.penup()
    draw.goto(-600, -300)
    draw.setheading(90)
    draw.pencolor('black')
    draw.fillcolor('brown')
    draw.begin_fill()
    draw.pendown()
    bedleg()
    draw.end_fill()
    draw.goto(-100, -300)
    draw.pendown()
    draw.begin_fill()
    bedleg()
    draw.end_fill()
    draw.fillcolor('red')
    draw.penup()
    draw.goto(-600, -250)
    draw.pendown()
    draw.begin_fill()
    for i in range(2):
        draw.forward(150)
        draw.right(90)
        draw.forward(520)
        draw.right(90)
    draw.end_fill()
    draw.fillcolor('white')
    draw.penup()
    draw.goto(-600, -100)
    draw.pendown()
    draw.begin_fill()
    for i in range(2):
        draw.forward(35)
        draw.right(90)
        draw.forward(150)
        draw.right(90)
    draw.end_fill()


def bedleg():
    for i in range(2):
        draw.forward(50)
        draw.right(90)
        draw.forward(20)
        draw.right(90)
        draw.penup()


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

# define basic the text turtle, which we will use to write, etc
textbub = turtle.Turtle()
textbub.penup()
textbub.hideturtle()
textbub.goto(0, 200)

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

# define the tree turtle
tree = turtle.Turtle()
tree.color('black')
tree.shape('turtle')
tree.speed('fastest')
tree.hideturtle()
tree.penup()

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
mainsitting.goto(-400, -100)


# define the flipped desk for scene 2
turtle.addshape('flipped_desk.gif')
flipped_desk = turtle.Turtle(shape='flipped_desk.gif')
flipped_desk.hideturtle()
flipped_desk.penup()

# add an event to the checkmark
checkmark.onclick(scene1)
turtle.mainloop()  # uncomment once you start doing turtle drawing
screen.mainloop()
