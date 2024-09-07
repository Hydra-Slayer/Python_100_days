from turtle import Turtle
from random import randint
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto(randint(-280,280),randint(-280,250))
        
    def eaten(self):
        self.goto(randint(-280,280),randint(-280,250))
        print("Food consumed") ## we can make score ++ after
    