from turtle import Turtle, Screen
import random
tutel = Turtle()

angle = 0
colors = ['red', 'blue', 'green', 'violet', 'black', 'yellow', 'brown', 'cyan', 'maroon', 'grey']
tutel.shape('turtle')

def draw_shape(sides):
    angle = 360 / sides
    for j in range(sides):
        tutel.forward(100)
        tutel.left(angle)

def set_color(turtle_obj):
    turtle_obj.pencolor(random.choice(colors))
    

for i in range(3,11):
    draw_shape(i)
    set_color(tutel)
    
        



    
screen = Screen()
screen.exitonclick()