import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Guesser")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")


# def get_coor(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_coor)
# turtle.mainloop()

def write(x,y,name):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.color("black")
    writer.penup()
    writer.goto(x,y)
    writer.write(f"{name}")


state_names= data["state"]

game_is_on = True
guessed_states = []
while game_is_on:
    answer = screen.textinput(title="Guess a state", prompt=f"What's a states name? {len(guessed_states)}/50 guessed")
    if answer == "exit":
        game_is_on = False
        break
    answer = answer.title()
    
    if answer in state_names.values:
        guessed_states.append(answer)
        state_coor = data[data["state"] == answer]
        write(int(state_coor["x"]), int(state_coor["y"]), answer)

states_missed =  []
for state in state_names.values:
    if state in guessed_states:
        continue
    else:
        states_missed.append(state)
        
new_data = pandas.DataFrame(states_missed)
new_data.to_csv("states_to_learn.csv")
screen.exitonclick()