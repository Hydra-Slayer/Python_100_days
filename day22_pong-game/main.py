from turtle import Turtle, Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



score_red = Scoreboard("left")

score_blue = Scoreboard("right")

score_red.draw_line()
p_red_score = 0
p_blue_score = 0

paddle_left = Paddle((250,0))
paddle_right = Paddle((-250,0))
paddle_left.color("blue")
paddle_right.color("red")

ball = Ball()

screen.listen()
screen.onkeypress(paddle_left.go_up,"Up")
screen.onkeypress(paddle_left.go_down,"Down")
screen.onkeypress(paddle_right.go_up,"w")
screen.onkeypress(paddle_right.go_down,"s")



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 215 or ball.ycor()<-250:
        ball.bounce_wall()
    if (ball.distance(paddle_right) < 100 and ball.xcor() < -230) or (ball.distance(paddle_left) < 100 and ball.xcor() > 230):
        ball.bounce_paddle()
        screen.update()
    
    if ball.xcor()> 280:
        ball.reset_pos()
        score_blue.update_score()
    if ball.xcor() < -280:
        ball.reset_pos()
        score_red.update_score()
        
    if score_blue.score>=7 or score_red.score >= 7:
        is_game_on = False
      
if   score_blue.score> score_red.score:
    score_red.game_over() 
    score_blue.win()
else:
    score_blue.game_over()
    score_red.win()
screen.exitonclick()

