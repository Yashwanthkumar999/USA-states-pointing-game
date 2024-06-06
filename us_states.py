import turtle as t

# from display import Display
import pandas

sc = t.Screen()

sc.title("us states game")
image = "blank_states_img.gif"
sc.addshape(image)
t.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# x_pos = data.x.to_list()
# y_pos = data.y.to_list()


guessed_states = []

# game_on = True


# for i in range(50):
#
#     answer_state = sc.textinput(title=f"{i}/50 Guess the state", prompt="what's the another state name?").lower()
#     for name in states:
#         if answer_state == name.lower():
#             pos = states.index(name)
#             new_pos = (x_pos[pos],y_pos[pos])
#             print(f"{name}'s position is{x_pos[pos]} , {y_pos[pos]}")
#             disp = Display(answer_state,new_pos)

while len(guessed_states) < 50:
    answer_state = sc.textinput(title=f"{len(guessed_states)}/50 states are correct",
                                prompt="what's the another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_tobe_learnt.csv")

        break
    if answer_state in states:
        guessed_states.append(answer_state)
        tom = t.Turtle()
        tom.hideturtle()
        tom.penup()
        state_pos = data[data.state == answer_state]
        tom.goto(int(state_pos.x), int(state_pos.y))
        tom.write(answer_state, align="center", font=("arial", 8, "normal"))
