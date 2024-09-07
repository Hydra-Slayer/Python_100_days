from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.score = 0
    
    def draw_line(self):
        drawer = Turtle()
        drawer.penup()
        drawer.goto(-300,250)
        drawer.pendown()
        drawer.pencolor("white")
        drawer.goto(300,250)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over...", align=ALIGNMENT,font=FONT)

    
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)