import turtle
import random

turns = [0, 90, 180, 270]
turtle.colormode(255)
tutel = turtle.Turtle()

tutel.speed(100)
disp = turtle.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    r_colors = (r,g,b)
    return r_colors

def go_about(obj):
    obj.circle(100)

def draw_spiro(obj,number_of_circles):
    
    for _ in range(number_of_circles):
        obj.color(random_color())
        obj.circle(100)
        curr_heading = obj.heading()
        obj.setheading(curr_heading+(360/number_of_circles))
   
draw_spiro(tutel,50)     
disp.exitonclick()