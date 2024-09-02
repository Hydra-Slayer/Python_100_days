from turtle import Turtle,Screen
from random import randint
screen = Screen()


screen.setup(width=500, height=500)

user_bet = screen.textinput(title="Tutrle Bookie",prompt="Place your bets: ")
is_race_on = False


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tutels = []
for color in colors:
    tutel = Turtle(shape="turtle")
    tutel.color(color)
    tutel.penup()
    tutel.goto(-230,(-120+40*colors.index(color)))
    tutels.append(tutel)
    
    


if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in tutels:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            break
            
        speed = randint(20,30)
        turtle.forward(speed)
        
if winning == user_bet:
                print(f"you win! Reward: 10$ {winning} turtle won!")
else: 
                print(F"You loose 10$ {winning} turtle won!")


            
screen.exitonclick()