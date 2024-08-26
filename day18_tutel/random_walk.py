import turtle
import random

turns = [0, 90, 180, 270]
turtle.colormode(255)
tutel = turtle.Turtle()
tutel.pensize(8)
tutel.speed(10)
disp = turtle.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    r_colors = (r,g,b)
    return r_colors

def go_about(obj):
    obj.circle(100)

def walk(obj):
    
    for _ in range(30):
        obj.color(random_color())
        obj.left(random.choice(turns))
        obj.forward(random.randint(50,150))
        
        
        
#walk(tutel)
go_about(tutel)
disp.exitonclick()