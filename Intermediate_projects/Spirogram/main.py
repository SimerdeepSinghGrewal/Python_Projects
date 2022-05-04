from turtle import Turtle, Screen
import random

def random_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return tim.color(R, G, B)

tim = Turtle()
# tim.color("chartreuse")
# sides=3
# for i in range(3, 11):
#     random_color()
#     angle = 360/sides
#     for j in range(0, sides):
#         tim.forward(100)
#         tim.left(angle)
#     for j in range(0, sides):
#         tim.forward(100)
#         tim.right(angle)
#     sides += 1

# tim = Turtle()
# tim.shape("turtle")
# for i in range(200):
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     tim.color(R, G, B)
#     tim.pen(pensize=7, speed=10)
#     angle = 90* random.randint(0, 3)
#     tim.forward(30)
#     tim.left(angle)


def draw_spirograph(angle):
    for i in range(int(360/angle)):
        random_color()
        tim.pen(pensize=2, speed=0)
        tim.circle(100)
        tim.setheading(tim.heading() + angle)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()