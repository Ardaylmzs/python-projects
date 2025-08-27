import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_user = screen.textinput(title=f"{len(guessed_states)}/50 states correct !",
                                   prompt="What is another state's name?").title()
    if answer_user == "Exit":
        missing_states =[state for state in all_states if not state in guessed_states] # this method list comprehension
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_user in all_states:
        print(answer_user)
        guessed_states.append(answer_user)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.state == answer_user]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_user)
screen.mainloop()