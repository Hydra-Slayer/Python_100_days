from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        
        self.shapesize(5.0,1.0)
        self.goto(position)
        
    def go_up(self):
        if self.ycor() < 190:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            pass
    def go_down(self):
        
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            pass