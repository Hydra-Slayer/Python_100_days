from turtle import Turtle, Screen

tutel = Turtle()

screen = Screen()

def move_fwd():
    tutel.forward(10)

def move_back():
    tutel.back(10)
    
def turn_left():
    tutel.left(10)
def turn_right():
    tutel.right(10)
def cl_sc():
    tutel.penup()
    tutel.clear()
    tutel.home()
    tutel.pendown()

screen.listen()
screen.onkeypress(move_fwd,"w")
screen.onkeypress(turn_left,"a")
screen.onkeypress(turn_right,"d")
screen.onkeypress(move_back,"s")
screen.onkeypress(cl_sc,"c")
screen.exitonclick()