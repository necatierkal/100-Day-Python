import random
from turtle import Turtle

import colorgram
import turtle



# colors = colorgram.extract('image.jpg',40) #image main ile aynı seviyede olmalı
# rgb_array=[]
# for item in colors:
#     r=item.rgb.r
#     g=item.rgb.g
#     b=item.rgb.b
#     rgb=(r,g,b)
#     rgb_array.append(rgb)
# print(rgb_array)


color_list=[(245, 239, 230), (251, 226, 233), (46, 92, 144), (243, 250, 245), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (233, 237, 244), (211, 56, 76), (155, 23, 19), (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), (163, 209, 182), (227, 171, 180), (17, 75, 108), (116, 123, 146), (184, 188, 208), (73, 79, 43), (162, 199, 214)]

tim = Turtle()

screen = turtle.Screen()
screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.goto(-250, 250)
for row in range(10):
    for col in range(10):
        tim.dot(20, random.choice(color_list))

        tim.forward(50)

    tim.penup()
    tim.goto(-250, 250 - (row + 1) * 50)


screen.exitonclick()
