# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('1.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
pos_x = 00
pos_y = -200
tim.up()
tim.hideturtle()
tim.speed("fastest")
for height in range(0, 10):
    tim.setposition((pos_x, pos_y))
    for length in range(0, 10):
        col = random.choice(color_list)
        tim.dot(20, col)
        tim.forward(50)
    pos_y +=50

screen = Screen()
screen.exitonclick()


