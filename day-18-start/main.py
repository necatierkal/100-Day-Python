import turtle
from idlelib.colorizer import color_config
from random import random, randint,choice
from turtle import Turtle,Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# for step in range(3,10):
#     for _ in range(step+1):
#         if step%2==0:
#             tim.forward(50)
#             if _ +1 <=step:
#                 tim.right(360/step)
#         else:
#             if _ +1 <= step:
#                 tim.right(360/step)
#                 if step>_+1:
#                     tim.forward(50)


# for step in range(3,11):
#     angle = 360/step
#     for _ in range(step):
#         tim.forward(100)
#         tim.right(angle)

# colors = ["cornflower blue","aquamarine","blue","yellow","dark slate blue","medium spring green","navy","yellow green"]
# directions = [0,90,180,270]
# tim.speed(10)
# tim.pensize(15)
#
# for item in range(150):
#     tim.setheading(choice(directions))
#     tim.forward(30)
#     tim.pencolor(choice(colors))
#

# turtle.reset()
#
# turtle.circle(5,5,5)
# turtle.shapesize(5,5)
# for item in range(36):
#     turtle.tilt(10)
#


# turtle.home()
# turtle.position()
#
# turtle.heading()
#
# turtle.circle(50)
# turtle.position()
#
# turtle.heading()
#
# turtle.circle(120, 180)  # draw a semicircle
# turtle.position()
#
# turtle.heading()





turtle.colormode(255)

def random_color():
    r= randint(0,255)
    g= randint(0,255)
    b= randint(0,255)

    color=(r,g,b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for item in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)












screen = Screen()
screen.exitonclick()

