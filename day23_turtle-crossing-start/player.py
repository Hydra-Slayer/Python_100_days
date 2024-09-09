from turtle import Turtle
class Player(Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(self.STARTING_POSITION)
        self.setheading(90)
    
    def cross(self):
        if self.ycor() >= 280:
            pass
            
        
        else:
            self.forward(self.MOVE_DISTANCE)
    def level_up(self):
        self.MOVE_DISTANCE *=1.1
    
    def reset(self):
        self.goto(0,-280)
    
