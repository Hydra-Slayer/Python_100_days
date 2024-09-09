import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.cross,"Up")


game_is_on = True
while game_is_on:
    if player.ycor() >= 280:
        scoreboard.level_up()
        player.level_up()
        player.reset()
    
    for car in carmanager.cars:
        if car.distance(player) < 30:
            game_is_on = False
    
    time.sleep(0.1)
    carmanager.add_car()
    carmanager.move_traffic()
    screen.update()
    
scoreboard.write()


screen.exitonclick()