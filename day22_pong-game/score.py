from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.side = side
        if side == "left":
            self.goto(70,250)
        else:
            self.goto(-70,250)
        self.color("white")
        self.score = 0
        self.ALIGNMENT = side
        self.speed("fastest")
        self.write(f"Score: {self.score}",align=self.ALIGNMENT, font=FONT)
    
    def draw_line(self):
        drawer = Turtle()
        drawer.penup()
        drawer.goto(-400,250)
        drawer.pendown()
        drawer.pencolor("white")
        drawer.goto(400,250)
    
    def game_over(self):
        if self.side == "left":
            self.goto(70,0)
        else:
            self.goto(-70,0)
        self.write("Game Over", align=self.ALIGNMENT,font=FONT)
    
    def win(self):
        if self.side == "left":
            self.goto(70,0)
        else:
            self.goto(-70,0)
        self.write("You won", align=self.ALIGNMENT,font=FONT)
    
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align=self.ALIGNMENT, font=FONT)