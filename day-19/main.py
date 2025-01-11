# from turtle import Turtle,Screen
#
#
# tim = Turtle()
# screen = Screen()
#
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# def turn_left():
#     new_heading = tim.heading() +10
#     tim.setheading(new_heading)
#
# def turn_right():
#     new_heading = tim.heading() -10
#     tim.setheading(new_heading)
#
#
# screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="a",fun=turn_left)
# screen.onkey(key="d",fun=turn_right)
#
# screen.onkey(key="c",fun=clear)
#
#
# screen.exitonclick()
import turtle


# Yarışçı kaplumbağalar
from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
height_variable = 0
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + height_variable)
    height_variable+=30
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
