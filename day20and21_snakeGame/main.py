from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()

#initialise screen events for keypress
screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")



scoreboard = Scoreboard()
scoreboard.draw_line()
scoreboard.update_score()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect food eaten
    if snake.head.distance(food)<15:
        
        food.eaten()
        snake.add_len()
        scoreboard.update_score()
        
    #detect ollision with tail
    if snake.is_tailbite():
        scoreboard.restart_game()
        snake.restart_game()
        scoreboard.update_score()
    #detet collosion with wall
    if snake.head.xcor() > 288 or snake.head.xcor()<-288 or snake.head.ycor()>250 or snake.head.ycor() <-288:
        scoreboard.restart_game()
        scoreboard.update_score()
        snake.restart_game()
    

scoreboard.reset()
screen.exitonclick()