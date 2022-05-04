from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
# def move_forward():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# def move_left():
#     tim.left(10)
# def move_right():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.up()
#     tim.home()
#     tim.down()
#
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")

for turtle_index in range(0, 6):
    y = [-60, -30, 0, 30, 60, 90]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            if user_bet == turtle.pencolor():
                print(f"You Won! {turtle.pencolor()} colored turtle won")
            else:
                print(f"You Lose. {turtle.pencolor()} colored turtle won.")
            is_race_on = False

        turtle.forward(random.randint(1, 10))

screen.exitonclick()
