import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# turtle.addshape(image)
# turtle.shape(image)
screen.bgpic(image)
turtle.penup()
turtle.hideturtle()
still_on = True
ans = 0
ans_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while still_on:
    answer_state = screen.textinput(title=f"{len(ans_states)}/50 Guess the state", prompt="What's another state's "
                                                                                          "name ?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in ans_states]
        data11 = pandas.DataFrame(missing_states)
        data11.to_csv("missing_states_data.csv")
        print(f"Your final score is {len(ans_states)}")
        break
    if len(data[data.state == answer_state]):
        ans_states.append(answer_state)
        cords = data[data.state == answer_state]
        x_cord = int(cords.x)
        y_cord = int(cords.y)
        turtle.goto(x_cord, y_cord)
        turtle.write(answer_state)
        ans += 1
        if ans == 50:
            still_on = False
            print("You guessed every state in USA. You Won!")
