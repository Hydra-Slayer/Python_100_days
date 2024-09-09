from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    level = 1
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-250,280)
        self.clear()
        self.write(f"Level: {self.level}", align="center",font=FONT)

        
    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", align="center",font=FONT)
             
    def game_over(self):
        self.clear()
        self.write(f"Level: {self.level}, Game over", align="center",font=FONT)
        