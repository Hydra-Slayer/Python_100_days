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
        self.score = -1
        with open("highscores.txt", "r") as file:
                file.seek(0)
                content = file.read().strip()  # Read and strip any extraneous whitespace
                if content:
                    self.high_score = int(content)  # Convert the content to an integer
                
        
    
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
        self.goto(0,250)
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)
        self.goto(150,250)
        self.write(f"Highest: {self.high_score}")
    
    def restart_game(self):
        if self.score > self.high_score :
            self.high_score= self.score
            with open("highscores.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = -1