from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager():
    cars = []
    MOVE_INCREMENT = 5
    def __init__(self) -> None:
        super().__init__()
        self.draw_line(270)
        self.draw_line(-262)
        
    def draw_line(self,height):
        drawer = Turtle()
        drawer.penup()
        drawer.goto(-300,height)
        drawer.pendown()
        drawer.pencolor("black")
        drawer.goto(300,height)
    
    def add_car(self):
        chance = randint(1,10)
        if chance != 2:
            pass
        else:
            new_car = Turtle()
            new_car.color(COLORS[randint(0,5)])
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.shape("square")
            random_y = randint(-250,250)
            new_car.setheading(180)
            new_car.goto(300,random_y)     
            self.cars.append(new_car)
        
    def move_traffic(self):
        for car in self.cars:
            if car.xcor()>300:
                self.cars.remove(car)
                pass
            else:
                car.forward(self.MOVE_INCREMENT)
    def level_ip(self):
        self.MOVE_INCREMENT *=1.05