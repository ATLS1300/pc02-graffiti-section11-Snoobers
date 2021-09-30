#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Seliskar
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny! Pizza time!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.up()

turtle.goto(-85, 150)

turtle.down()

turtle.begin_fill()

turtle.color("black")

turtle.forward(100)

turtle.right(25)

turtle.forward(75)

turtle.undo()

turtle.forward(50)

turtle.right(45)

turtle.right(30)

turtle.forward(20)

turtle.forward(20)

turtle.right(90)

turtle.forward(50)

turtle.undo()

turtle.forward(40)

turtle.right(75)

turtle.forward(25)

turtle.left(90)

turtle.forward(10)

turtle.left(75)

turtle.forward(25)

turtle.right(90)

turtle.forward(50)

turtle.forward(50)

turtle.undo()

turtle.forward(25)

turtle.forward(5)

turtle.right(75)

turtle.forward(40)

turtle.end_fill()

turtle.up()

turtle.color("brown")

turtle.right(110)

turtle.forward(45)

turtle.undo()

turtle.forward(30)

turtle.right(90)

turtle.right(90)

turtle.forward(25)

turtle.undo()

turtle.forward(15)

turtle.left(90)

turtle.forward(10)

turtle.right(20)

turtle.left(45)

turtle.left(45)

turtle.forward(25)

turtle.left(25)

turtle.down()

turtle.circle(20)

turtle.undo()

turtle.right(90)

turtle.forward(10)

turtle.undo()

turtle.undo()

turtle.undo()

turtle.undo()

turtle.undo()

turtle.up()

turtle.forward(20)

turtle.right(45)

turtle.forward(10)

turtle.circle(8)

turtle.right(180)

turtle.forward(5)

turtle.circle(8)

turtle.right(90)

turtle.circle(10)

turtle.forward(20)

turtle.right(10)

turtle.right(15)

turtle.right(90)

turtle.forward(10)

turtle.left(100)

turtle.forward(20)

turtle.circle(10)

turtle.left(180)

turtle.forward(30)

turtle.right(180)

turtle.circle(10)

turtle.forward(10)

turtle.begin_fill()

turtle.circle(10)

turtle.down()

turtle.circle(10)

turtle.end_fill()

turtle.down()

turtle.begin_fill()

turtle.circle(10)

turtle.end_fill()

turtle.end_fill()

turtle.up()

turtle.forward(75)

turtle.right(180)

turtle.forward(10)

turtle.right(180)

turtle.forward(15)

turtle.down()

turtle.begin_fill()

turtle.circle(10)

turtle.end_fill()

turtle.up()

turtle.color("black")

turtle.left(180)

turtle.forward(100)

turtle.forward(10)

turtle.forward(10)

turtle.forward(10)

turtle.forward(10)

turtle.right(90)

turtle.forward(15)

turtle.forward(10)

turtle.right(90)

turtle.down()

turtle.forward(25)

turtle.up()

turtle.up()

turtle.forward(100)

turtle.forward(100)

turtle.forward(100)

turtle.left(180)

turtle.forward(400)

turtle.right(180)

turtle.right(90)

turtle.forward(20)

turtle.forward(10)

turtle.left(90)

turtle.forward(50)

turtle.forward(10)

turtle.right(90)

turtle.down()

turtle.forward(20)

turtle.right(80)

turtle.left(170)

turtle.forward(25)

turtle.left(90)

turtle.forward(25)

turtle.left(15)

turtle.forward(10)

turtle.left(75)

turtle.forward(20)

turtle.left(10)

turtle.forward(10)

turtle.left(90)

turtle.forward(30)

turtle.begin_fill()

turtle.forward(10)

turtle.left(75)

turtle.forward(30)

turtle.left(90)

turtle.forward(50)

turtle.left(90)

turtle.forward(30)

turtle.forward(30)

turtle.undo()

turtle.forward(10)

turtle.left(45)

turtle.forward(10)

turtle.left(45)

turtle.right(45)

turtle.left(90)

turtle.forward(25)

turtle.end_fill()

turtle.right(45)

turtle.begin_fill()

turtle.forward(25)

turtle.left(90)

turtle.right(180)

turtle.forward(10)

turtle.right(75)

turtle.forward(50)

turtle.right(90)

turtle.right(10)

turtle.right(10)

turtle.forward(25)

turtle.right(90)

turtle.forward(20)

turtle.end_fill()

turtle.right(180)

turtle.forward(90)

turtle.undo()

turtle.pensize(10)

turtle.forward(90)

turtle.undo()

turtle.pensize(20)

turtle.forward(90)

turtle.right(45)

turtle.forward(20)

turtle.forward(40)

turtle.right(30)

turtle.forward(40)

turtle.right(45)

turtle.forward(10)

turtle.undo()

turtle.left(20)

turtle.forward(40)

turtle.right(20)

turtle.forward(30)

turtle.right(45)

turtle.forward(40)

turtle.forward(20)

turtle.forward(30)

turtle.forward(10)

turtle.up()

turtle.forward(200)

turtle.forward(10)

turtle.left(90)

turtle.right(180)

turtle.right(10)

turtle.right(10)

turtle.forward(10)

turtle.right(180)

turtle.color("brown")

turtle.forward(200)

turtle.undo()

turtle.begin_fill()

turtle.forward(300)

turtle.undo()

turtle.down()

turtle.forward(300)

turtle.left(180)

turtle.pensize(4)

turtle.color("DeepPink4")

turtle.forward(250)

turtle.forward(40)

turtle.forward(40)

turtle.undo()

turtle.forward(15)

turtle.up()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
